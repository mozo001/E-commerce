from django.contrib import admin  # type: ignore
from django.urls import path 
from .views import home_page_view

urlpatterns = [
    path('', home_page_view),  # type: ignore[arg-type]
]   
