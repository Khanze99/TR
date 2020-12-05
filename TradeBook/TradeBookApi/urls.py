from django.urls import path

from .views import CategoryAPI

urlpatterns = [

    path('categorys', CategoryAPI.as_view(), name='categories')

]