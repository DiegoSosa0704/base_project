from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

router = DefaultRouter()
router.register('user', views.UserRegisterDRF, base_name='users')

urlpatterns = [
    path('login/', views.TokenView.as_view(), name="token"),
] + router.urls