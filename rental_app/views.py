from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet
from .permissions import IsAdminOrReadOnly, IsCustomer

# generic views
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError


class CarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    

class AvailableCarListView(generics.ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    
    def get_queryset(self):
        start_date = self.request.query_params.get('start_date')
        end_date = self.request.query_params.get('end_date')
        if not start_date or not end_date:
            data = {'WARNING': "PLEASE provide BOTH start_date and end_date parameters!"}
            return Car.objects.none(), data
        queryset = Car.objects.all()
        reserved_cars = Car.objects.filter(reservations__start_date__lt=end_date)
        queryset = queryset.exclude(pk__in=reserved_cars)
        return queryset, {}
    
    def list(self, request, *args, **kwargs):
        queryset, extra_data = self.get_queryset()
        serializer = self.get_serializer(queryset, many = True)
        response_data = serializer.data
        return Response((response_data, extra_data), status=status.HTTP_200_OK)

class ReservationListView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = [IsCustomer]
    
    def perform_create(self, serializer):
        start_date = serializer.validated_data.get('start_date')
        end_date = serializer.validated_data.get('end_date')
        
        user = self.request.user
        
        existing_reservations = Reservation.objects.filter(user=user, start_date=start_date, end_date=end_date)
        
        if existing_reservations.exists():
            raise ValidationError("You already have a reservation for this time period!")

        serializer.save()
    
# ModelViewSet to consolidate the code, but reduces ease of customization

class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes =  [IsAdminOrReadOnly]
    

class ReservationViewSet(ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes =  [IsAdminOrReadOnly]