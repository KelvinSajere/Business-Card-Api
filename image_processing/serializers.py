from django.conf import settings
from django.core.files.storage import FileSystemStorage
from rest_framework import serializers


class BusinessCardSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    business_name = serializers.CharField(max_length=256)
    client_name = serializers.CharField(max_length=256)
    role = serializers.CharField(max_length=256)
    phone_number = serializers.CharField(max_length=256)
    email = serializers.CharField(max_length=256)
    website = serializers.CharField(max_length=256)
    address = serializers.CharField(max_length=256)


class FileUploadSerializer(serializers.Serializer):
    file = serializers.ImageField(allow_empty_file=False)

    def save(self):
        file = self.validated_data['file']
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)
        return uploaded_file_url
