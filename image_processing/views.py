from django.contrib.auth.models import Group, User
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response

from image_processing.models import BusinessCard

from . import serializers

cards = {
    1: BusinessCard(id=1, business_name='Konoha Academy Business', client_name='Naruto', role='Ninja', phone_number="123123123", email="naruto@gmail.com", website="www.gogoanime.com", address="Konoha"),
    2: BusinessCard(id=2, business_name='Konoha Academy', client_name='Naruto', role='Ninja', phone_number="123123123", email="naruto@gmail.com", website="www.gogoanime.com", address="Konoha"),
    3: BusinessCard(id=3, business_name='Konoha Academy', client_name='Naruto', role='Ninja', phone_number="123123123", email="naruto@gmail.com", website="www.gogoanime.com", address="Konoha"),
}


class BusinessCardViewSet(viewsets.ViewSet):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.BusinessCardSerializer

    def list(self, request):
        serializer = serializers.BusinessCardSerializer(
            instance=cards.values(), many=True)
        return Response(serializer.data)
