from django.db import models, phone
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Address(models.Model):
    """
    Represents an address model.

    Attributes:
        street (CharField): The street or house number of the address.
        city (CharField): The city of the address.
        state (CharField): The state or region of the address.
        zipcode (CharField): The postal code of the address.
    """
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=10)

class Person(models.Model):
    """
    Represents a person model with various details.

    Attributes:
        name (CharField): The name of the person.
        dob (DateField): The date of birth of the person (nullable and optional).
        email (EmailField): The email address of the person (nullable and optional).
        phone_number (PhoneNumberField): The phone number of the person.
        profile_picture (ImageField): The profile picture of the person (nullable and optional).
        person_address (OneToOneField): A one-to-one relationship with the Address model for the person's address (nullable and optional).
    """
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = PhoneNumberField()
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    person_address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)




