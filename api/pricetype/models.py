from django.db import models

class Pricetype(models.Model):
    name = models.CharField(primary_key=True, unique=True, max_length=100)
    price = models.BooleanField(blank=True, default=False,  )
    bid = models.BooleanField(blank=True, default=False,  )
    bidoptional = models.BooleanField(blank=True, default=False,  )
    payment = models.BooleanField(blank=True, default=False,  )
    buybuttontxt = models.TextField(blank=True, null=True)
    pricetagtxt = models.TextField(blank=True, null=True)