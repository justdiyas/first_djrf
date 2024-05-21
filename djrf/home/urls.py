from django.urls import path
from . import views

urlpatterns = [
    path('person/', views.person, name='person_api'),
    path('person/<int:person_id>/', views.person_delete, name='person_delete_api'),
    path('login/', views.login, name='login'),
    path('person-view/', views.PersonView.as_view(), name='person_view'),
    path('person-view/<int:id>', views.PersonDeleteView.as_view(), name='person_delete'),
]