from .models import *
from rest_framework import serializers


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"
        
        
        
class ReservationSerializer(serializers.ModelSerializer):
    car_plate_number = serializers.CharField(source='car.plate_number', read_only=True)
    class Meta:
        model = Reservation
        fields = "__all__"
    