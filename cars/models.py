from django.db import models

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Car(models.Model):
    car_model = models.CharField(max_length=50)
    car_condition = models.CharField(max_length=200)
    Manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return self.car_model