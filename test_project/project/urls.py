from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from project import views

router = DefaultRouter()
router.register(r'home', views.home ,basename = 'home')


urlpatterns = [
    path("", include(router.urls)),

]
