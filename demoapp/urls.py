from django.urls import path
from . import views

urlpatterns= [
    path("hotel_list/", views.Hotels_list, name="hotelList"),
]