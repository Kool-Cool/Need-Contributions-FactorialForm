""" creating model form """

from django.forms import ModelForm
from . import models

class FactForm(ModelForm):
    class Meta:
        model = models.Number # Giving model which we want to use
        fields = "__all__"