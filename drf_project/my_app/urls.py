from django.urls import path
from .views.main_view import product_view,product_view_detail

urlpatterns = [
    path('product/',product_view),
    path('product/<int:id>/',product_view_detail)
]
