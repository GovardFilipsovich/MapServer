from django.shortcuts import render
from django.views import View
from rest_framework import viewsets


# Create your views here.
# listings/views.py

from .forms import *
from .serializers import *


class MapsViewSet(viewsets.ModelViewSet):
    queryset = MapModel.objects.all()
    serializer_class = MapSerializer


class MapCreateView(View):
    def get(self, request):
        return render(
            request, "maps/add_map.html", {"mapForm": MapForm(), "infoForm": InfoForm()}
        )

    def post(self, request):
        map_form = MapForm(request.POST, request.FILES)
        map_ = map_form.save(commit=False)
        info_form = InfoForm(request.POST)
        info_ = info_form.save()
        map_.info = info_
        map_form.save()

        return render(
            request,
            "maps/add_map.html",
            {"mapForm": map_form, "infoForm": info_form},
        )
