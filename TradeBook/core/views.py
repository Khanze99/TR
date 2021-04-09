from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CategorySerializer
from .models import Category


class CategoryAPI(APIView):

    def get(self, request):

        result = []
        categories = Category.objects.filter(parent__isnull=True)

        for category in categories:
            subcategories = category.get_children()
            serializer_category = CategorySerializer(category).data
            serializer_subcategories = CategorySerializer(subcategories, many=True).data
            serializer_category['subcategories'] = serializer_subcategories
            result.append(serializer_category)

        return Response(result, status=200)


def main(request):
    return render(request, 'main.html')
