from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.CategoryView.as_view()),
    path('products',views.ProductView.as_view()),
    path('category/<int:category_id>/products',views.CategoryProductsView.as_view())
]