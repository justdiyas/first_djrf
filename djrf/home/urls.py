from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index_api'),
    path('person/', views.person, name='person_api'),
    path('person/delete/<int:person_id>/', views.person_delete, name='person_delete_api'),
]