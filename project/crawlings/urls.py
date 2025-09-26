from django.urls import path
from . import views

app_name = 'crawlings'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('delete/<int:crawling_pk>/', views.delete, name='delete'),
]