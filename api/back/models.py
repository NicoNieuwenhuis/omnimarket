from django.db import models

class Theme(models.Model):
    id = models.AutoField(primary_key=True)
    banner = models.FileField()
    logo = models.FileField()
    favicon = models.FileField()
    bannertext = models.CharField(max_length=100)