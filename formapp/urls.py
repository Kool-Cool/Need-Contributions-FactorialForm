from django.contrib import admin
from django.urls import path

from . import views



urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.home_page_view,name="Home"),
    
    path("fact",views.factorial_view ,name="factorial"),
    # path("",views.HomePageView.as_view() , name= "Home")
    
]