from django.conf import settings
from django.db import models

# ------------ REFERENCE TABLES ------------

class AircraftType(models.Model):
     manufacturer = models.CharField()
     model = models.CharField()
     effective_range = models.FloatField()
     cruising_speed = models.FloatField()
     capacity = models.IntegerField()
    
class Airline(models.Model):
    name = models.CharField()
    short_name = models.CharField()

class Country(models.Model):
    name = models.CharField()
    continent = models.CharField()
    currency = models.CharField()

class Tariff(models.Model):
    code = models.CharField()
    name = models.CharField()

class Airport(models.Model):
    country_id = models.ForeignKey(Country, on_delete = models.CASCADE)
    name = models.CharField()
    iata_short = models.CharField()
    icao_short = models.CharField()
    timezone = models.CharField()

# ------------ REFERENCE TABLES END ------------
    

class Reservation(models.Model):
    created = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class Flight(models.Model):
    departure_airport_id = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name = 'departure_airport_id')
    arrival_airport_id = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name = 'arrival_airport_id')
    airline_id = models.ForeignKey(Airline, on_delete = models.CASCADE)
    aircraft_type_id = models.ForeignKey(AircraftType, on_delete = models.CASCADE)
    tariff_id = models.ForeignKey(Tariff, on_delete = models.CASCADE)
    departure_timestamp = models.DateTimeField()
    arrival_timestamp = models.DateTimeField()

class FlightReservation(models.Model):
    reservation_id = models.ForeignKey(Reservation, on_delete = models.CASCADE)
    flight_id = models.ForeignKey(Flight, on_delete = models.CASCADE)