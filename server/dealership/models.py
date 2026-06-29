from django.db import models
from django.contrib.auth.models import User


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

    def __str__(self):
        return self.name


class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='carmodels')
    dealer_id = models.IntegerField()
    name = models.CharField(max_length=100)
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('HATCHBACK', 'Hatchback'),
        ('CONVERTIBLE', 'Convertible'),
        ('TRUCK', 'Truck'),
        ('VAN', 'Van'),
    ]
    car_type = models.CharField(max_length=20, choices=CAR_TYPES)
    year = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f'{self.car_make.name} {self.name}'


class CarDealer(models.Model):
    dealer_id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    st = models.CharField(max_length=50, blank=True)
    lat = models.FloatField(default=0.0)
    long = models.FloatField(default=0.0)

    def __str__(self):
        return self.full_name


class DealerReview(models.Model):
    dealership = models.ForeignKey(CarDealer, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=100)
    purchase = models.BooleanField(default=False)
    review = models.TextField()
    purchase_date = models.DateField(null=True, blank=True)
    car_make = models.CharField(max_length=100, blank=True)
    car_model = models.CharField(max_length=100, blank=True)
    car_year = models.IntegerField(null=True, blank=True)
    sentiment = models.CharField(max_length=20, blank=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Review by {self.name} for dealer {self.dealership_id}'
