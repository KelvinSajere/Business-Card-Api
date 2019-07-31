from rest_framework.parsers import FileUploadParser, MultiPartParser, FormParser
from django.contrib.gis import views
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from image_processing.models import BusinessCard

from . import serializers

cards = {
    1: BusinessCard(id=1, business_name='Konoha Academy Business', client_name='Naruto', role='Ninja', phone_number="123123123", email="naruto@gmail.com", website="www.gogoanime.com", address="Konoha"),
    2: BusinessCard(id=2, business_name='Konoha Academy', client_name='Naruto', role='Ninja', phone_number="123123123", email="naruto@gmail.com", website="www.gogoanime.com", address="Konoha"),
}


class BusinessCardView(views.APIView):
    # Required for the Browsable API renderer to have a nice form.
    serializer_class = serializers.FileUploadSerializer
    parser_class = [MultiPartParser, FormParser]

    def get(self, request):
        serializer = serializers.BusinessCardSerializer(
            instance=cards.values(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):

        file_serializer = serializers.FileUploadSerializer(
            data=request.data)
        if file_serializer.is_valid():
            file = file_serializer.save()
            return Response({'file': file}, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
