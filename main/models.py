from django.db import models

# Create your models here.
class Answers(models.Model):
    prenume = models.CharField(max_length = 100)
    family_name = models.CharField(max_length=100)
    email = models.EmailField(unique = True, max_length = 100)
    phone_number = models.CharField(max_length = 15, unique = True, default = "0000000000")
    message = models.CharField(max_length = 3750)
    public_ip_address = models.GenericIPAddressField(unique = True)
    has_submitted_cookie = models.BooleanField(default = False)