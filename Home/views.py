import datetime

from django.shortcuts import render, render_to_response
from django.template import RequestContext

from .models import ProjectDetail
from . import forms
from . import models


# Create your views here.
def home(request):
    project_detail = ProjectDetail.objects.all().order_by('position', 'period_start')
    context = {'project_detail': project_detail}
    customer_form = forms.CustomerDetailForm()
    if request.method == 'POST':
        form = forms.CustomerDetailForm(request.POST)
        if form.is_valid():
            print(form.data.values())
            form.save()
            context = {'message': 'We will Contact you @ {} .... 😊'.format(form.data['email']),
                       'project_detail': project_detail,
                       'form': customer_form}
            return render(request, 'Home/index.html', context)
    context = {'project_detail': project_detail}
    customer_form = forms.CustomerDetailForm()
    context.update({
        'form': customer_form
    })
    return render(request, 'Home/index.html', context)


def dip(request):
    return render(request, 'Home/dip.html')


def aos(request):
    return render(request, 'Home/aos000.html')
