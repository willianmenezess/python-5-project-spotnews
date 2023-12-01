from django.urls import path
from news.views import home, news_details, register_category


urlpatterns = [
    path('', home, name='home-page'),
    path('news/<int:id>/', news_details, name='news-details-page'),
    path('categories/', register_category, name='categories-form'),
]
