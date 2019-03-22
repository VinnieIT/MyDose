from django.urls import path
from MyDose import views

urlpatterns = [
    path("", views.home, name="home"),
]