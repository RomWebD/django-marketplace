from django.urls import path
from .views import (
    index,
    product_list_view,
    category_list_view,
    category_product_list_view,
    vendor_detail_view,
    vendor_list_view,
    product_detail_view,
)


app_name = "core"
urlpatterns = [
    path("", index, name="index"),
    path("products/", product_list_view, name="product-list"),
    path("categories/", category_list_view, name="category-list"),
    path("category/<name>/<cid>/", category_product_list_view, name="category-product-list"),
    path("vendors/", vendor_list_view, name="vendor-list"),
    path("vendor/<vid>", vendor_detail_view, name="vendor-detail"),
    path("product/<pid>", product_detail_view, name="product-detail"),
]
