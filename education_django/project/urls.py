from django.urls import path

from project import views

urlpatterns = [
    path('', views.get_projects),
    path('get_categories/', views.get_categories),
    path('<slug:slug>/', views.get_project),
    path('create/', views.create_project),
]


    