from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import PermissionRequiredMixin

# Create your views here.
def prod_list(request, category_id=None):
    category = None
    products = Product.objects.filter(available=True)
    if category_id:
        category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=category, available=True)
    
    paginator = Paginator(products, 9)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage, InvalidPage):
        products = paginator.page(paginator.num_pages)

    return render(request, 'car/category.html', {'category':category, 'prods':products})

def product_detail(request, category_id, product_id):
    product = get_object_or_404(Product, category_id=category_id, id=product_id)
    return render(request, 'car/product.html', {'product':product})

class CarCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'car.add_car'
    model = Product
    fields = ('name', 'description', 'category', 'price', 'image', 'stock', 'available')
    template_name = 'car/car_new.html'
