from django.contrib import admin
from django.urls import path
from experiences import views

urlpatterns = [
    path("", views.experience, name="experiences"),
    path("create/", views.create, name="create"),
]