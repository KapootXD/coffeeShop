from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("CoffeeShop is live ☕")
# Create your views here.
