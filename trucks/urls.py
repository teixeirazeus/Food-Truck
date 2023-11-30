from django.contrib import admin
from django.urls import path
from .views import FoodTruckListView

urlpatterns = [
    path("", FoodTruckListView.as_view(), name="food-truck"),
]
