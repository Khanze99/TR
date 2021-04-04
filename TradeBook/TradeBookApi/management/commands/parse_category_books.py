import requests
from bs4 import BeautifulSoup


from django.core.management.base import BaseCommand
from django.conf import settings


from TradeBookApi.models import Category


class Command(BaseCommand):
    help = 'Parsing book categories'

    def handle(self, *args, **options):

        Category.objects.all().delete()

        url = settings.LIB_CATEGORIES_URL
        result = requests.get(url)
        html = result.text

        soup = BeautifulSoup(html, 'lxml')
        ul_genre_list = soup.find('ul', class_='genre-list')

        categories = [h2.text for h2 in ul_genre_list.find_all('h2')]
        sublist = [tag.text.strip() for tag in ul_genre_list.find_all('ul', class_='genre-sublist')]
        subcategories = list(map(lambda categories: categories.split('\n'), sublist))
        category_dict = dict(zip(categories, subcategories))

        for category in enumerate(category_dict, 1):
            cat_model = Category.objects.create(id=category[0], name=category[1])
            for subcategory in category_dict[category[1]]:
                Category(name=subcategory, parent=cat_model).save()
