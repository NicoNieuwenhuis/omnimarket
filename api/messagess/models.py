from django.db import models
from django_userforeignkey.models.fields import UserForeignKey
from django.conf import settings

class Conversation(models.Model):
    subject = models.CharField(max_length=150)
    timestamp = models.DateTimeField(auto_now_add=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, related_name="messages", on_delete=models.CASCADE)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="receiver", on_delete=models.CASCADE)
    sender = UserForeignKey(auto_user_add=True, null=True, blank=True, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-timestamp']
