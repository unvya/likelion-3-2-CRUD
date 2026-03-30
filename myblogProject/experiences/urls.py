from django.contrib import admin
from django.urls import path
from experiences import views

urlpatterns = [
    path("", views.experience, name="experiences"),
    path("create/", views.create, name="create"),
    path("<int:post_id>/", views.experience_detail, name="experience_detail"),
    path("experience_update/<int:id>/", views.experience_update, name="experience_update"),
    path("experience_delete/<int:id>/", views.experience_delete, name="experience_delete"),
]