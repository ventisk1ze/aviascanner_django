from scanner.serializers import CountrySerializer, TariffSerializer, AirportSerializer, AirlineSerializer, \
    AircraftTypeSerializer, UserSerializer
from .models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response


# ------------------------- REFERENCE VIEWS -------------------------
class CountriesList(APIView):
    """
    List all countries
    """

    def get(self, request):
        countries = Country.objects.all()
        serializer = CountrySerializer(countries, many=True)
        return Response(serializer.data)


class TariffsList(APIView):
    """
    List all tariffs
    """

    def get(self, request):
        countries = Tariff.objects.all()
        serializer = TariffSerializer(countries, many=True)
        return Response(serializer.data)


class AircraftTypesList(APIView):
    """
    List all aircraft types
    """

    def get(self, request):
        countries = AircraftType.objects.all()
        serializer = AircraftTypeSerializer(countries, many=True)
        return Response(serializer.data)


class AirportsList(APIView):
    """
    List all airports
    """

    def get(self, request):
        countries = Airport.objects.all()
        serializer = AirportSerializer(countries, many=True)
        return Response(serializer.data)


class AirlinesList(APIView):
    """
    List all airlines
    """

    def get(self, request):
        countries = Airline.objects.all()
        serializer = AirlineSerializer(countries, many=True)
        return Response(serializer.data)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            return Response(data={'error_message': 'User not found'}, status=status.HTTP_401_UNAUTHORIZED)

        if not user.check_password(password):
            return Response(data={'error_message': 'Password incorrect'}, status=status.HTTP_401_UNAUTHORIZED)