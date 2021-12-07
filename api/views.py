from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("This is the Flights tracker API, to get all the flights use the endpoint /flights")
