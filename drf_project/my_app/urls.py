from django.urls import path
from .views.main_view import product_view

urlpatterns = [
    path('product/',product_view)
]
