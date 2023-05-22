from django.db import models

# Create your models here.django-admin --version
from django.db import models


class Agency(models.Model):
    agency_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    logo = models.BinaryField(null=True)
    city = models.CharField(max_length=20, null=True)
    postal_code = models.PositiveSmallIntegerField(null=True)
    street = models.CharField(max_length=45, null=True)
    street_number = models.CharField(max_length=45, null=True)
    email = models.EmailField(max_length=100, null=True)
    phone = models.CharField(max_length=45, null=True)


class Flight(models.Model):
    flight_id = models.PositiveIntegerField(primary_key=True)
    departure_date = models.DateTimeField()
    arrival_date = models.DateTimeField()
    aircraft_id = models.PositiveIntegerField()
    origin = models.PositiveIntegerField()
    destination_id = models.PositiveIntegerField()


class Aircraft(models.Model):
    aircraft_id = models.PositiveIntegerField(primary_key=True)
    model_number = models.PositiveSmallIntegerField(null=True)
    manufacturer = models.CharField(max_length=30, null=True)
    agency_id = models.PositiveIntegerField()


class Ticket(models.Model):
    ticket_id = models.PositiveIntegerField(primary_key=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    passenger_id = models.PositiveIntegerField()


class Airport(models.Model):
    airport_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=45, null=True)
    city = models.CharField(max_length=30, null=True)


class BoardingPass(models.Model):
    boarding_pass_id = models.PositiveIntegerField(primary_key=True)
    gate = models.PositiveSmallIntegerField()
    status = models.CharField(max_length=3, null=True)
    flight_id = models.PositiveIntegerField()
    ticket_id = models.PositiveIntegerField()


class Passenger(models.Model):
    passenger_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(max_length=45, null=True)
    phone = models.CharField(max_length=45, null=True)


class Pilot(models.Model):
    pilot_id = models.PositiveIntegerField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)


class PilotFlight(models.Model):
    pilot_id = models.PositiveIntegerField()
    flight_id = models.PositiveIntegerField()

    class Meta:
        unique_together = (("pilot_id", "flight_id"),)
