from typing import List
from ..models import *
from django.core.exceptions import ObjectDoesNotExist
import json


def add_flights(data) -> List[Itinerary]:
    for l in data["legs"]:
        departure_airport = None
        arrival_airport = None
        airline = None
        try:
            departure_airport = Airport.objects.get(
                code=l["departure_airport"])
        except ObjectDoesNotExist:
            departure_airport = Airport.objects.create(code=l["departure_airport"])
        try:
            arrival_airport = Airport.objects.get(code=l["arrival_airport"])
        except ObjectDoesNotExist:
            arrival_airport = Airport.objects.create(code=l["arrival_airport"])
        try:
            airline = Airline.objects.get(id=l["airline_id"])
        except ObjectDoesNotExist:
            airline = Airline.objects.create(id=l["airline_id"], name=l["airline_name"])

        leg = Leg(
            id=l["id"],
            departure_airport=departure_airport,
            arrival_airport=arrival_airport,
            departure_time=l["departure_time"],
            arrival_time=l["arrival_time"],
            stops=l["stops"],
            airline=airline,
            duration_mins=l["duration_mins"]
        )
        leg.save()
    for i in data["itineraries"]:
        agent = None
        try:
            agent = Agent.objects.get(name=i["agent"])
        except ObjectDoesNotExist:
            agent = Agent.objects.create(name=i["agent"], rating=i["agent_rating"])

        itinerary = Itinerary(
            id=i["id"],
            price=i["price"],
            agent=agent
        )
        itinerary.save()
        leg1 = Leg.objects.get(id=i["legs"][0])
        leg2 =  Leg.objects.get(id=i["legs"][1])
        itinerary.legs.set([leg1, leg2])

def get_flights():
    itineraries = []
    for i in list(Itinerary.objects.all()):
        legs = list(i.legs.all())
        itineraries.append({
            "id": i.id,
            "legs": [
                {
                    "id": legs[0].id
                },
                {
                    "id": legs[1].id
                }
            ],
            "price": i.price,
            "agent": i.agent.name
        })
    return itineraries

def get_flights_price(price: int):
    itineraries = []
    for i in list(Itinerary.objects.all()):
        legs = list(i.legs.all())
        if int(i.price[1:]) > price:
            itineraries.append({
                "id": i.id,
                "legs": [
                    {
                        "id": legs[0].id
                    },
                    {
                        "id": legs[1].id
                    }
                ],
                "price": i.price,
                "agent": i.agent.name
            })
    return itineraries

