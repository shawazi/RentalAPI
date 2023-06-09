from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Car(models.Model):
    TRANSMISSION_OPTIONS = (
        ("A", "Automatic"),
        ("M", "Manual")
    )
    
    plate_number = models.CharField(max_length=15)
    make = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    year = models.IntegerField()
    transmission = models.CharField(options=TRANSMISSION_OPTIONS, max_length=1)
    rent_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    out_of_service = models.BooleanField()
    
    def __str__(self):
        return f"{self.make} {self.model} {self.year} {self.plate_number} {self.transmission} {self.rent_per_day} {self.out_of_service}"
    
class Reservation(models.Model):
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    car = models.ForeignKey(Car, on_delete=models.PROTECT)
    customer = models.ForeignKey(User, on_delete=models.PROTECT)
    
    def __str__(self):
        return f"{self.customer} {self.car} {self.start_date} {self.end_date}"