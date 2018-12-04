import datetime

from django.shortcuts import render


# Create your views here.
def home(request):
    messages = ""
    date = datetime.datetime(year=2018, month=11, day=1) - datetime.datetime.now()
    if request.method == 'POST':
        messages = "We will contact you soon."

    days = date.days
    hours = date.seconds // 3600
    minutes = (date.seconds // 60) % 60
    print(days)
    print(hours)
    print(minutes)
    return render(request, 'Home/home.html', {
        'messages': messages,
        'days': days,
        'hours': hours,
        'minutes': minutes,
    })
