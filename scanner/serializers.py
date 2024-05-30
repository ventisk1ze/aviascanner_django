from rest_framework import serializers
from django.conf import settings
from .models import AircraftType, Airline, Country, Tariff, Airport, Reservation, Flight, FlightReservation


class AircraftTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AircraftType
        fields = ['manufacturer', 'model', 'effective_range', 'cruising_speed', 'capacity']


class AirlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airline
        fields = ['name', 'short_name']


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ['name', 'continent', 'currency']


class TariffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tariff
        fields = ['code', 'name']


class AirportSerializer(serializers.ModelSerializer):
    country_id = CountrySerializer()

    class Meta:
        model = Airport
        fields = ['country_id', 'name', 'iata_short', 'icao_short', 'timezone']


class ReservationSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()

    class Meta:
        model = Reservation
        fields = ['created', 'user']


class FlightSerializer(serializers.ModelSerializer):
    departure_airport_id = AirportSerializer()
    arrival_airport_id = AirportSerializer()
    airline_id = AirlineSerializer()
    aircraft_type_id = AircraftTypeSerializer()
    tariff_id = TariffSerializer()

    class Meta:
        model = Flight
        fields = ['departure_airport_id', 'arrival_airport_id', 'airline_id', 'aircraft_type_id', 'tariff_id', 'departure_timestamp', 'arrival_timestamp']


class FlightReservationSerializer(serializers.ModelSerializer):
    reservation_id = ReservationSerializer()
    flight_id = FlightSerializer()

    class Meta:
        model = FlightReservation
        fields = ['reservation_id', 'flight_id']