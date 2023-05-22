from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

# Create your views here.

# def home_page_view(request):
#     return HttpResponse("Hellow World !!")

class HomePageView(TemplateView):
    template_name = "home.html"