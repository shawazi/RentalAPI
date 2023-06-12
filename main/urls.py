
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("rental_app.urls")),
    path('account/', include('account_app.urls')),
]
    