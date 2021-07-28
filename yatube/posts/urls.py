# posts/urls.py
from django.urls import path

from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('group/', views.group, name = 'group_index'),
    path('group/<slug:slug>/', views.group_posts, name='group')
]