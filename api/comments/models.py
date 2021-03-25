from __future__ import unicode_literals
from django_userforeignkey.models.fields import UserForeignKey
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.urls import reverse
from listings.models import Listing
from users.models import CustomUser


class Comment(models.Model):
    author = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.CASCADE)
    listing       = models.ForeignKey(Listing, related_name="listing", null=True, blank=True, on_delete=models.CASCADE)
    content     = models.TextField()
    timestamp   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.listing.name

    def get_absolute_url(self):
        return reverse("comments:thread", kwargs={"id": self.id})

    def get_delete_url(self):
        return reverse("comments:delete", kwargs={"id": self.id})
        



