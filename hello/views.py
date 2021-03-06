from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from .models import Greeting

import sys

sys.path
sys.executable

import requests
import datetime
import csv

# Create your views here.
def index(request):
    return render(request, "index.html")

def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})

# @csrf_exempt
def get_data(request, state = "nv"):

    client = requests.session()
    client.get('https://coronavirusapi.com/users/sign_in').cookies

    temp = client.get('https://coronavirusapi.com/users/sign_in').content.decode()

    csrftoken = temp[temp.find('csrf-token') + 21 : temp.find('==')] + '=='
    login = {'user[email]': 'bryanlubay1@gmail.com','user[password]': 'FUCK355th!@#$', 'authenticity_token' : csrftoken} 
    post_request = client.post('https://coronavirusapi.com/users/sign_in', data=login)

    response = client.get("http://coronavirusapi.com/getTimeSeries/" + state + "/")

    data = response.text
    data = data.replace('\n',',')
    data = data.split(',')
    epoch = []
    tested = []
    positive = []
    deaths = []

    counter = 0
    for i in data:
        if counter == 0:
            epoch.append(i)            
        elif counter == 1:
            tested.append(i)
        elif counter == 2:
            positive.append(i)
        else:
            deaths.append(i)

        counter += 1
        if counter == 4:
            counter = 0

    return JsonResponse(data={'Date' : epoch, 'Tested' : tested, 'Positive' : positive, 'Deaths' : deaths}, status=200)