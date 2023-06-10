from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# from rest_framework.permissions import IsAdminUser

from .permissions import IsAdminOrReadOnly

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes =  [IsAdminOrReadOnly]
    

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes =  [IsAdminOrReadOnly]