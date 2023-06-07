from django.db import models

# Create your models here.

GENDER_SELECTION = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)

SERVICE_SELECTION = (
    ('Renter', 'Renter'),
    ('Rentee', 'Rentee'),
)

class UserInfo(models.Model):
    created = models.DateField(auto_now_add=True)
    full_name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20, choices=GENDER_SELECTION)
    address = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField(max_length=50)
    service = models.CharField(max_length=20, choices=SERVICE_SELECTION)