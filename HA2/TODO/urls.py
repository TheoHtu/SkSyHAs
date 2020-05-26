from django.urls import path

from . import views

urlpatterns = [
    path('', views.Main.as_view(), name='main'),
    path('edit/', views.edit, name='edit'),
    path('edit/save', views.save, name='save'),
    path('delete/', views.delete, name='delete'),
    path('add/', views.Add.as_view(), name='add'),
    path('add/new/', views.new_todo, name='create'),
    path('impressum/', views.Impressum.as_view(), name='imp'),
]
