from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):
    # by default, there is a field called id which is the pk of the table, so no need to specify it
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    # email = models.EmailField()
    zipcode = models.CharField(max_length=5)

class Quote(models.Model):
    # by default, there is a field called id which is the pk of the table, so no need to specify it
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField()
    address = models.CharField(max_length=100)
    gallons = models.IntegerField()
    total_price = models.DecimalField(max_digits=20, decimal_places=4)