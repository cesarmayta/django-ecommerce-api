from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.CategoryView.as_view()),
    path('products',views.ProductView.as_view())
]