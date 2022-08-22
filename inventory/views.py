from django.shortcuts import render
from .models import Product
from django.core.paginator import Paginator


def all_products(request):
    products = Product.objects.all()
    paginator = Paginator(products, 6)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)
    context = {'page_obj': page_obj}

    return render(request, 'inventory/output.html', context)