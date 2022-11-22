from django.views.generic import ListView
from .model import Car

# Create your views here.
class CarListView(ListView):
    model = Car
    template_name = 'home.html'
    context_object_name = 'all_cars_list'