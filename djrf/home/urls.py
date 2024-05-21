from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('person-viewset', views.PersonViewSet, basename='person')


urlpatterns = [
    path('', include(router.urls)),
    path('person/', views.person, name='person_api'),
    path('person/<int:person_id>/', views.person_delete, name='person_delete_api'),
    path('login/', views.login, name='login'),
    path('person-view/', views.PersonView.as_view(), name='person_view'),
    path('person-view/<int:id>', views.PersonDeleteView.as_view(), name='person_delete'),
]