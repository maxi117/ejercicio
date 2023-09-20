from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def vista2(request):
    return HttpResponse("<h1>vista 2 app2</h1>")