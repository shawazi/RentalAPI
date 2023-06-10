
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("car", CarViewSet)
router.register("reservation", ReservationViewSet)

urlpatterns = [

] + router.urls
