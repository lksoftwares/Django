from django.db import models
class contactModel(models.Model):
    Name=models.CharField(max_length=50)
    Contact_No=models.CharField(max_length=50)
    email=models.EmailField()
    Address=models.CharField(max_length=100)


