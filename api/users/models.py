from django.contrib.auth.models import AbstractUser
from django.db import models
from autoslug import AutoSlugField
from django.core.validators import RegexValidator
import uuid

alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters and numbers are allowed.')

class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, editable=False)
    admin = models.BooleanField(default=False)
    new = models.BooleanField(default=False)
    msgnoti = models.BooleanField(default=True)
    othernoti = models.BooleanField(default=True)
    paynoti = models.BooleanField(default=True)
    adds = models.BooleanField(default=False)
    username = models.CharField(max_length=100, primary_key=True, unique=True, blank=False, validators=[alphanumeric])
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='username', unique=True, validators=[alphanumeric])
    member_since = models.DateTimeField(auto_now_add=True)
    profilepic = models.FileField(null=True)
    phone_number = models.DecimalField(max_digits=12, decimal_places=0, null=True)
    about_you = models.CharField(max_length=1000, null=True)