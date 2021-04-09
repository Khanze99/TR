from django.urls import path

from .views import CategoryAPI

urlpatterns = [

    path('categories/', CategoryAPI.as_view(), name='categories'),

]