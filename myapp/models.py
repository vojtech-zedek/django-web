from django.db import models

class Agency(models.Model):
    agency_id = models.PositiveIntegerField(primary_key=True, verbose_name='Agency ID', help_text='Enter the agency ID')
    name = models.CharField(max_length=45, verbose_name='Name', help_text='Enter the agency name')
    logo = models.BinaryField(null=True, verbose_name='Logo')
    city = models.CharField(max_length=20, null=True, verbose_name='City', help_text='Enter the city')
    postal_code = models.PositiveSmallIntegerField(null=True, verbose_name='Postal Code', help_text='Enter the postal code')
    street = models.CharField(max_length=45, null=True, verbose_name='Street', help_text='Enter the street')
    street_number = models.CharField(max_length=45, null=True, verbose_name='Street Number', help_text='Enter the street number')
    email = models.EmailField(max_length=100, null=True, verbose_name='Email', help_text='Enter the email')
    phone = models.CharField(max_length=45, null=True, verbose_name='Phone', help_text='Enter the phone number')

    class Meta:
        ordering = ['name']
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'

    def __str__(self):
        return self.name


class Flight(models.Model):
    flight_id = models.PositiveIntegerField(primary_key=True, verbose_name='Flight ID', help_text='Enter the flight ID')
    departure_date = models.DateTimeField(verbose_name='Departure Date', help_text='Enter the departure date')
    arrival_date = models.DateTimeField(verbose_name='Arrival Date', help_text='Enter the arrival date')
    aircraft_id = models.PositiveIntegerField(verbose_name='Aircraft ID', help_text='Enter the aircraft ID')
    origin = models.PositiveIntegerField(verbose_name='Origin', help_text='Enter the origin')
    destination_id = models.PositiveIntegerField(verbose_name='Destination ID', help_text='Enter the destination ID')

    class Meta:
        ordering = ['departure_date']
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

    def __str__(self):
        return f'Flight {self.flight_id}'


class Aircraft(models.Model):
    aircraft_id = models.PositiveIntegerField(primary_key=True, verbose_name='Aircraft ID', help_text='Enter the aircraft ID')
    model_number = models.PositiveSmallIntegerField(null=True, verbose_name='Model Number', help_text='Enter the model number')
    manufacturer = models.CharField(max_length=30, null=True, verbose_name='Manufacturer', help_text='Enter the manufacturer')
    agency_id = models.PositiveIntegerField(verbose_name='Agency ID', help_text='Enter the agency ID')

    class Meta:
        ordering = ['manufacturer', 'model_number']
        verbose_name = 'Aircraft'
        verbose_name_plural = 'Aircrafts'

    def __str__(self):
        return f'Aircraft {self.aircraft_id}'


class Ticket(models.Model):
    ticket_id = models.PositiveIntegerField(primary_key=True, verbose_name='Ticket ID', help_text='Enter the ticket ID')
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Price', help_text='Enter the price')
    passenger_id = models.PositiveIntegerField(verbose_name='Passenger ID', help_text='Enter the passenger ID')

    class Meta:
        ordering = ['price']
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return f'Ticket {self.ticket_id}'


class Airport(models.Model):
    airport_id = models.PositiveIntegerField(primary_key=True, verbose_name='Airport ID', help_text='Enter the airport ID')
    name = models.CharField(max_length=45, null=True, verbose_name='Name', help_text='Enter the airport name')
    city = models.CharField(max_length=30, null=True, verbose_name='City', help_text='Enter the city')

    class Meta:
        ordering = ['name']
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'

    def __str__(self):
        return self.name


class BoardingPass(models.Model):
    boarding_pass_id = models.PositiveIntegerField(primary_key=True, verbose_name='Boarding Pass ID', help_text='Enter the boarding pass ID')
    gate = models.PositiveSmallIntegerField(verbose_name='Gate', help_text='Enter the gate number')
    status = models.CharField(max_length=3, null=True, verbose_name='Status', help_text='Enter the status')
    flight_id = models.PositiveIntegerField(verbose_name='Flight ID', help_text='Enter the flight ID')
    ticket_id = models.PositiveIntegerField(verbose_name='Ticket ID', help_text='Enter the ticket ID')

    class Meta:
        ordering = ['gate']
        verbose_name = 'Boarding Pass'
        verbose_name_plural = 'Boarding Passes'

    def __str__(self):
        return f'Boarding Pass {self.boarding_pass_id}'


class Passenger(models.Model):
    passenger_id = models.PositiveIntegerField(primary_key=True, verbose_name='Passenger ID', help_text='Enter the passenger ID')
    first_name = models.CharField(max_length=45, verbose_name='First Name', help_text='Enter the first name')
    last_name = models.CharField(max_length=45, verbose_name='Last Name', help_text='Enter the last name')
    email = models.EmailField(max_length=45, null=True, verbose_name='Email', help_text='Enter the email')
    phone = models.CharField(max_length=45, null=True, verbose_name='Phone', help_text='Enter the phone number')

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Passenger'
        verbose_name_plural = 'Passengers'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pilot(models.Model):
    pilot_id = models.PositiveIntegerField(primary_key=True, verbose_name='Pilot ID', help_text='Enter the pilot ID')
    first_name = models.CharField(max_length=45, verbose_name='First Name', help_text='Enter the first name')
    last_name = models.CharField(max_length=45, verbose_name='Last Name', help_text='Enter the last name')

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Pilot'
        verbose_name_plural = 'Pilots'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PilotFlight(models.Model):
    pilot_id = models.PositiveIntegerField(verbose_name='Pilot ID', help_text='Enter the pilot ID')
    flight_id = models.PositiveIntegerField(verbose_name='Flight ID', help_text='Enter the flight ID')

    class Meta:
        unique_together = (("pilot_id", "flight_id"),)
        verbose_name = 'Pilot Flight'
        verbose_name_plural = 'Pilot Flights'
        
    def __str__(self):
        return f'Pilot Flight {self.flight_id}'
        


