from django.db import models
from phone_field import PhoneField
from django.core.validators import RegexValidator
from phonenumber_field.modelfields import PhoneNumberField


class Requests(models.Model):
    full_name = models.CharField(max_length=100)
    msisdn = PhoneNumberField()
    email = models.EmailField(null=True)
    comments = models.TextField(null=True, blank=True)
    agreement = models.BooleanField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
