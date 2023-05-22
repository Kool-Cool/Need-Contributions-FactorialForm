""" creating model form """

from django.forms import ModelForm
from . import models

class FactForm(ModelForm):
    class Meta:
        model = models.Number
        fields = "__all__"