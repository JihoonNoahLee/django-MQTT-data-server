from django.db import models

# Create your models here.
class Data(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    temperature = models.FloatField()
    humidity = models.FloatField()
