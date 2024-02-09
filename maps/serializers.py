from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ["author", "address", "description"]

class MapSerializer(serializers.ModelSerializer):
    info = InfoSerializer(many=False)
    class Meta:
        model = MapModel
        fields = ["name", "preview", "image", "info"]
