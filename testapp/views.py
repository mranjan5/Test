from django.shortcuts import render
import datetime
from django.http import HttpResponse
# Create your views here.
def date_time_view(request):
    date=datetime.datetime.now()
    s='<h1> The current date and time at server is:'+str(date)+'</h1>'
    return HttpResponse(s)
def hello_world_view(request):
    return HttpResponse('<h1> hello wel come to banagelore </h1>')
