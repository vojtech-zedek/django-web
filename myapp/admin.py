from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Agency, Flight, Aircraft, Ticket, Airport, BoardingPass, Passenger, Pilot, PilotFlight

admin.site.register(Agency)
admin.site.register(Flight)
admin.site.register(Aircraft)
admin.site.register(Ticket)
admin.site.register(Airport)
admin.site.register(BoardingPass)
admin.site.register(Passenger)
admin.site.register(Pilot)
admin.site.register(PilotFlight)