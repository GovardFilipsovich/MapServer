from django import forms

from .models import *


class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = "__all__"


class AsTextFileInput(forms.widgets.FileInput):
    def value_from_datadict(self, data, files, name):
        print("-------------------------")
        print(files)
        string = files.get(name).read().decode("utf-8")
        return " ".join(string.split()) 


class MapForm(forms.ModelForm):
    class Meta:
        model = MapModel
        exclude = ("info",)
        widgets = {"preview": AsTextFileInput(), "image": AsTextFileInput()}
