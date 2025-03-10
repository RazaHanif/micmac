from django.contrib import admin

from .models import Airport, Flight, Passenger

# Register your models here.

# Set up your own configure files (django docs to learn)

# Read up in django docs for what can be done 

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination", "duration")

class PassengerAdmin(admin.ModelAdmin):
    filter_horizontal = ("flights",) 


admin.site.register(Airport)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Passenger, PassengerAdmin)
