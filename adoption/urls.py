# adoption/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.animal_list, name='animal_list'),  # Set this as the default page
    path('form/', views.adoption_form, name='adoption_form'),
    path('animal/edit/<int:animal_id>/', views.animal_edit, name='animal_edit'),
]
