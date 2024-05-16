from django.urls import path
from . import views

urlpatterns = [
    path('person/', views.person, name='person_api'),
    path('person/<int:person_id>/', views.person_delete, name='person_delete_api'),
]