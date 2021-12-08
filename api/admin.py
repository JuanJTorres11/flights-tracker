from django.contrib import admin
from .task import retrieve_data
from .models import *

class ItineraryAdmin(admin.ModelAdmin):
   list_display = ('id', 'price', 'agent', 'leg1', 'leg2')


admin.site.register(Agent)
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Leg)
admin.site.register(Itinerary, ItineraryAdmin)
retrieve_data()