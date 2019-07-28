from django.db import models


# Create your models here.
class BusinessCard():
    def __init__(self, id, business_name, client_name, role, phone_number, email, website, address):
        self.id = id
        self.business_name = business_name
        self.client_name = client_name
        self.role = role
        self.phone_number = phone_number
        self.email = email
        self.website = website
        self.address = address
