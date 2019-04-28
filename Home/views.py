import datetime

from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'Home/index.html')


def dip(request):
    return render(request, 'Home/dip.html')

def aos(request):
    return render(request, 'Home/aos.html')

