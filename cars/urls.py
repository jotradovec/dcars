from django.urls import path
from . import views

prefix = "cars"

urlpatterns = [
    path(prefix+'/', views.cars, name=prefix),
]

