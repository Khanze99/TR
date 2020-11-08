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

        category = [h2.text for h2 in ul_genre_list.find_all('h2')]
        sublist = [tag.text.strip() for tag in ul_genre_list.find_all('ul', class_='genre-sublist')]
        subcategory = list(map(lambda categories: categories.split('\n'), sublist))

        category_dict = dict(zip(category, subcategory))

        for cat in enumerate(category_dict, 1):
            cat_model = Category.objects.create(id=cat[0], name=cat[1])
            for subcat in category_dict[cat[1]]:
                Category(name=subcat, parent=cat_model).save()
