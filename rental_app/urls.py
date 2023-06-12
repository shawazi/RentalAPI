
from .views import *
from rest_framework.routers import DefaultRouter
from django.urls import path

router = DefaultRouter()
router.register("car", CarViewSet)
router.register("reservation", ReservationViewSet)


urlpatterns = [
    path('availablecars/', AvailableCarListView.as_view()),
    
] + router.urls


