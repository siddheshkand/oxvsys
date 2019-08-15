import datetime

from django.shortcuts import render
from .models import ProjectDetail


# Create your views here.
def home(request):
    project_detail = ProjectDetail.objects.all().order_by('position', 'period_start')
    context = {'project_detail': project_detail}
    return render(request, 'Home/index.html', context)


def dip(request):
    return render(request, 'Home/dip.html')


def aos(request):
    return render(request, 'Home/aos000.html')
