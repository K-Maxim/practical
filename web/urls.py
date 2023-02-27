from django.contrib import admin
from django.urls import path, include

from web.views import letter, all_letters, find_letter, check_letter, between_letters, get_some

urlpatterns = [
    path('letter/', all_letters, name='letters'),
    path('letter/<letter>/', letter, name='letter'),
    path('find/', find_letter, name='letter'),
    path('check/<letter>/<word>/', check_letter),
    path('between/', between_letters),
    path('get-some/<int:number>/', get_some),
    ]