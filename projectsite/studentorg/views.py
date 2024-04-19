from django.shortcuts import render
from django.urls import path
from studentorg.views import HomePageView
from studentorg import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.HomePageView.as_view(), name = 'home'),
]
# Create your views here.
