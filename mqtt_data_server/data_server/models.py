from django.db import models

# Create your models here.
class Data(models.Model):
    date = models.DateTimeField("날짜", max_length=19, null=False, unique=True)
    temperature = models.FloatField("온도", null=True)
    humidity = models.FloatField("습도", null=True)
