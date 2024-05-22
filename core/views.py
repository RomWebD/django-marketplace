from django.shortcuts import render
from django.db.models import Count

# Create your views here.
from core.models import Product, Category, Vendor
import logging

logger = logging.getLogger(__name__)


def index(request):
    products = Product.objects.filter(product_status="published", featured=True)
    context = {"products": products}
    return render(request, "core/index.html", context)


def product_list_view(request):
    products = Product.objects.filter()
    context = {"products": products}
    return render(request, "core/shop.html", context)


def category_list_view(request):
    # categories = Category.objects.all()
    categories = Category.objects.all().annotate(product_count=Count("category"))
    context = {"categories": categories}
    return render(request, "core/category-list.html", context)


def category_product_list_view(request, name, cid):
    category = Category.objects.get(cid=cid)
    products = Product.objects.filter(
        product_status="published", featured=True, category=category
    )
    context = {"category": category, "products": products}
    return render(request, "core/category-product-list.html", context)


def vendor_list_view(request):
    vendors = Vendor.objects.all()
    context = {"vendors": vendors}

    return render(request, "core/vendor-list.html", context)


def vendor_detail_view(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    products = Product.objects.filter(
        product_status="published", featured=True, vendor=vendor
    )
    context = {"vendor": vendor, "products": products}
    return render(request, "core/vendor-detail.html", context)


def product_detail_view(request, pid):
    try:
        product = Product.objects.get(pid=pid)
        p_image = product.p_images.all()
        context = {"product": product, "p_image": p_image}
        return render(request, "core/product-detail.html", context)
    except Exception as error:
        logger.error("This is an error message.")
