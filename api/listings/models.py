from django.db import models
from django.conf import settings
from users.models import CustomUser
from django_userforeignkey.models.fields import UserForeignKey
from autoslug import AutoSlugField
from django.core.validators import RegexValidator
from mptt.models import MPTTModel, TreeForeignKey

from pricetype.models import Pricetype

import auto_prefetch

alphanumeric = RegexValidator(r'^[0-9a-zA-Z ]+$', 'Only numbers, spaces and alphabetic characters are allowed.')

class Listing(auto_prefetch.Model):
    # pricetype choises
    pricetype = auto_prefetch.ForeignKey(Pricetype, null=True, on_delete=models.CASCADE)
    pricetext = models.CharField(max_length=100, blank=True, null=True )
    buybuttontxt = models.TextField(blank=True, null=True)
    hasprice = models.BooleanField(blank=True, default=False,  )
    payment = models.BooleanField(blank=True, default=False,  )
    bid = models.BooleanField(blank=True, default=False,  )
    # Listing description
    name = models.CharField(max_length=100, validators=[alphanumeric])
    price = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0.00, blank=True)
    firstimage = models.FileField(blank=True,)
    secondimage = models.FileField(blank=True,)
    description = models.TextField(blank=True, null=True)
    # Other data
    category = TreeForeignKey('categorys.Category', related_name='category', on_delete=models.CASCADE)
    # Logistic
    pickup = models.BooleanField(blank=True, default=False,  )
    delivery = models.BooleanField(blank=True, default=False,  )
    deliverycost = models.DecimalField(max_digits=6, decimal_places=2, null=True, default=0.00, blank=True)
    # Other data
    author = UserForeignKey(auto_user_add=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='name', validators=[alphanumeric])

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        url = reverse('listing', kwargs={'pk': self.pk, 'slug': self.get_slug()})
        return url


class ListingImage(models.Model):
    listing = models.ForeignKey(Listing, related_name='images',blank=True, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/%Y/%m/%d/', blank=True)

    def __str__(self):
        return self.listing.name