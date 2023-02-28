from django.contrib import admin
from django.urls import path, include

from web import views

urlpatterns = [
    path('letter/', views.all_letters, name='letters'),
    path('letter/<letter>/', views.letter, name='letter'),
    path('find/', views.find_letter, name='letter'),
    path('check/<letter>/<word>/', views.check_letter),
    path('between/', views.between_letters),
    path('get-some/<int:number>/', views.get_some),
    path('letters/', views.limit_letters),
    path('letters/page/<int:page>/', views.page_letters),
    path('search/', views.search),
    path('get/', views.get_len),
    ]