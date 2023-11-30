import math
from django.shortcuts import render
from .models import FoodTruck
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from .serializers import FoodTruckSerializer
from .models import FoodTruck
from django.core.serializers import serialize


class FoodTruckListView(APIView):
    def get(self, request):
        name = request.query_params.get("name")
        latitude = request.query_params.get("latitude")
        longitude = request.query_params.get("longitude")
        top_n = request.query_params.get("top_n", None)

        if name:
            trucks = FoodTruck.objects.filter(applicant__icontains=name)
        elif latitude and longitude and top_n:
            trucks = self.get_nearest_trucks(
                float(latitude), float(longitude), int(top_n)
            )
        else:
            trucks = FoodTruck.objects.all()

        serializer = FoodTruckSerializer(trucks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_nearest_trucks(self, lat, lon, top_n):
        trucks = FoodTruck.objects.all()
        for truck in trucks:
            truck.distance = self.calculate_distance(
                lat, lon, truck.latitude, truck.longitude
            )
        return sorted(trucks, key=lambda x: x.distance)[:top_n]

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = (
            math.sin(dlat / 2) ** 2
            + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
        )
        c = 2 * math.asin(math.sqrt(a))
        r = 6371  # Radius of Earth in kilometers
        return c * r
