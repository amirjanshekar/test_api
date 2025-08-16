from django.urls import path

from products.api.v1 import views

app_name = "v1.products"

urlpatterns = [
    path("", views.ProductsListView.as_view(), name="products"),
]
