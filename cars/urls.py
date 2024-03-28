from django.urls import path
from . import views

prefix = "cars"

urlpatterns = [
    path('', views.main, name=prefix),
    path(prefix+'/', views.cars, name=prefix),
    path(prefix+'/<int:id>', views.details, name='details'),
]

