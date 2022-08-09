"""BMS_PRO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from BMS_Apps.RelayOperations.views import device_listener,get_devices_status,main_update
import threading
import time
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView
from socket import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="BMS 2.0",
      default_version='v2',
      description="API for BMS 2.0",
    #   terms_of_service="https://www.google.com/policies/terms/",
    #   contact=openapi.Contact(email="contact@snippets.local"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include ([
        path('user-operations/',include('BMS_Apps.Users.api_urls')),
        path('bms-operations/',include('BMS_Apps.BMS_Main.api_urls')),
        path('areas-operations/',include('BMS_Apps.Areas.api_urls')),
        path('pantry-operations/',include('BMS_Apps.FoodOrdering.api_urls')),
        path('assets-operations/',include('BMS_Apps.StoreAssets_Management.api_urls')),
        path('inventory-operations/',include('BMS_Apps.InventoryManagement.api_urls')),
        path('audioAnnouncementSystem-operations/',include('BMS_Apps.AudioAnnouncementSystem.api_urls')),
        path('conference_room_booking-operations/',include('BMS_Apps.ConferenceRoomBooking.api_urls')),
    ])),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

# socket for udp sender
UDP_SENDER=socket(AF_INET, SOCK_DGRAM)
UDP_SENDER.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

# socket for udp listener
UDP_LISTENER=socket(AF_INET, SOCK_DGRAM)
UDP_LISTENER.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

# udp listener bind port 6000 and universal host 0.0.0.0
UDP_LISTENER.bind(('0.0.0.0', 6000))

# threading for device listener
# thread_relays = threading.Thread(target=device_listener)
# thread_relays.start()

# get_devices_status()

# time.sleep(2)

# jsonUpdator = threading.Thread(target=main_update)
# jsonUpdator.start()
