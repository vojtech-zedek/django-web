from django.db import models


class Agency(models.Model):
    name = models.CharField(max_length=45, verbose_name='Name', help_text='Enter the agency name', unique=True)
    logo = models.ImageField(upload_to='agency_logos', null=True, verbose_name='Logo')
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
    departure_date = models.DateTimeField(verbose_name='Departure Date', help_text='Enter the departure date')
    arrival_date = models.DateTimeField(verbose_name='Arrival Date', help_text='Enter the arrival date')
    aircraft = models.ForeignKey('Aircraft', on_delete=models.CASCADE, verbose_name='Aircraft', help_text='Select the aircraft')
    origin = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='departures', verbose_name='Origin', help_text='Select the origin airport')
    destination = models.ForeignKey('Airport', on_delete=models.CASCADE, related_name='arrivals', verbose_name='Destination', help_text='Select the destination airport')

    class Meta:
        ordering = ['departure_date']
        verbose_name = 'Flight'
        verbose_name_plural = 'Flights'

    def __str__(self):
        return f'Flight {self.pk}'


class Aircraft(models.Model):
    model_number = models.PositiveSmallIntegerField(null=True, verbose_name='Model Number', help_text='Enter the model number')
    manufacturer = models.CharField(max_length=30, null=True, verbose_name='Manufacturer', help_text='Enter the manufacturer')
    agency = models.ForeignKey('Agency', on_delete=models.CASCADE, verbose_name='Agency', help_text='Select the agency')

    class Meta:
        ordering = ['manufacturer', 'model_number']
        verbose_name = 'Aircraft'
        verbose_name_plural = 'Aircrafts'

    def __str__(self):
        return f'Aircraft {self.pk}'


class Ticket(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name='Price', help_text='Enter the price')
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE, verbose_name='Passenger', help_text='Select the passenger')

    class Meta:
        ordering = ['price']
        verbose_name = 'Ticket'
        verbose_name_plural = 'Tickets'

    def __str__(self):
        return f'Ticket {self.pk}'


class Airport(models.Model):
    name = models.CharField(max_length=45, null=True, verbose_name='Name', help_text='Enter the airport name')
    city = models.CharField(max_length=30, null=True, verbose_name='City', help_text='Enter the city')

    class Meta:
        ordering = ['name']
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'

    def __str__(self):
        return self.name


class BoardingPass(models.Model):
    gate = models.PositiveSmallIntegerField(verbose_name='Gate', help_text='Enter the gate number')
    status = models.CharField(max_length=3, null=True, verbose_name='Status', help_text='Enter the status')
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, verbose_name='Flight', help_text='Select the flight')
    ticket = models.ForeignKey('Ticket', on_delete=models.CASCADE, verbose_name='Ticket', help_text='Select the ticket')

    class Meta:
        ordering = ['gate']
        verbose_name = 'Boarding Pass'
        verbose_name_plural = 'Boarding Passes'

    def __str__(self):
        return f'Boarding Pass {self.pk}'


class Passenger(models.Model):
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
    first_name = models.CharField(max_length=45, verbose_name='First Name', help_text='Enter the first name')
    last_name = models.CharField(max_length=45, verbose_name='Last Name', help_text='Enter the last name')

    class Meta:
        ordering = ['last_name', 'first_name']
        verbose_name = 'Pilot'
        verbose_name_plural = 'Pilots'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class PilotFlight(models.Model):
    pilot = models.ForeignKey('Pilot', on_delete=models.CASCADE, verbose_name='Pilot', help_text='Select the pilot')
    flight = models.ForeignKey('Flight', on_delete=models.CASCADE, verbose_name='Flight', help_text='Select the flight')

    class Meta:
        unique_together = (("pilot", "flight"),)
        verbose_name = 'Pilot Flight'
        verbose_name_plural = 'Pilot Flights'

    def __str__(self):
        return f'Pilot Flight {self.flight.pk}'
        


