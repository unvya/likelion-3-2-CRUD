from django.contrib import admin
from django.urls import path
from letters import views

urlpatterns = [
    path("", views.letter, name="letters"),
]
