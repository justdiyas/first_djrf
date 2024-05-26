from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('person-viewset', views.PersonViewSetAPI, basename='person')

urlpatterns = [
    path('', include(router.urls)),
    path('person/', views.person, name='person_api'),
    path('person/<int:person_id>/', views.person_delete, name='person_delete_api'),
    path('login/', views.UserLoginAPI.as_view(), name='login'),
    path('person-view/', views.PersonAPI.as_view(), name='person_view'),
    path('person-view/<int:pk>', views.PersonDeleteAPI.as_view(), name='person_delete'),
    path('user-register/', views.UserRegisterAPI.as_view(), name='user_register'),
]