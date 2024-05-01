from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "webpage/home.html")

def analyze(request):
    return render(request, "webpage/analyze.html")

def group(request):
    return render(request, "webpage/group.html")

