from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from .services import logic


def index(request):
    return HttpResponse("This is the Flights tracker API, to get all the flights use the endpoint /flights")

def get_flights(request):
    flights = logic.get_flights()
    if flights:
        return JsonResponse(flights, safe=False)
    else:
        return JsonResponse({"Respuesta": "No hay vuelos registrados"})

def get_flights_price(request, price):
    flights = logic.get_flights_price(price)
    if flights:
        return JsonResponse(flights, safe=False)
    else:
        return JsonResponse({"Respuesta": f"No hay vuelos que hayan costado más de {price}"})