from django.urls import path
from . import views
from .views import CarCreateView

app_name = 'car'

urlpatterns = [
    path('', views.prod_list, name = 'all_products'),
    path('<uuid:category_id>/', views.prod_list, name = 'products_by_category'),
    path('<uuid:category_id>/<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('new/', CarCreateView.as_view(), name='car_create'),
]
