from django import forms
from .models import AdminInformation


class DataForm(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    address = forms.CharField()

class AdminData(forms.ModelForm):
    class Meta:
        model = AdminInformation
        fields = "__all__"