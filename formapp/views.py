from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

from .forms import FactForm #new 

# Create your views here.

def home_page_view(request):
    
    form = FactForm()
    
    print(request)
    context = {'form':form}
    return render(request , "home.html" , context)

# class HomePageView(TemplateView):
#     template_name = "home.html"