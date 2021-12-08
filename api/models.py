from django.db import models
from django.contrib import admin


class Agent(models.Model):
    name = models.CharField(max_length=50, unique=True)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    def __str__(self):
        return f"{self.name}"
class Airline(models.Model):
    id = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=50, unique=True)

class Airport(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
class Leg(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    departure_airport = models.ForeignKey(Airport, related_name='departure_legs', on_delete=models.PROTECT)
    arrival_airport = models.ForeignKey(Airport, related_name='arrival_legs',on_delete=models.PROTECT)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    stops = models.PositiveSmallIntegerField()
    airline = models.ForeignKey(Airline, on_delete=models.PROTECT)
    duration_mins = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.id}"

class Itinerary(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    price = models.CharField(max_length=10)
    agent = models.ForeignKey(Agent, on_delete=models.PROTECT)
    legs = models.ManyToManyField(Leg)

    @admin.display
    def leg1(self):
        return self.legs.all()[0]
    @admin.display
    def leg2(self):
        return self.legs.all()[1]