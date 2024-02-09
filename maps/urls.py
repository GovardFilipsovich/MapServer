from django.urls import path, include

from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"api/maps", MapsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("api/add_map", MapCreateView.as_view(), name="map-create"),
]
