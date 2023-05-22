from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

from .forms import FactForm #new 

# Create your views here.



def home_page_view(request):
    form = FactForm()
    # print(request)
    context = {'form':form}
    return render(request , "home.html" , context)


""" http://127.0.0.1:8000/factorial/15 """

def factorial(number):
    if number==0:
        return 1 
    else :
        return number*factorial(number-1)
    
    
def factorial_view(request):
    number = request.GET["Number"] # Hooolllyyyy
    result = factorial(int(number))
    return HttpResponse(f"The factorial of {number} is {result}")

# class HomePageView(TemplateView):
#     template_name = "home.html"
