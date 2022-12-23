from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100, blank=True, null=True)


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE ,related_name='measurement')
    temperature = models.FloatField()
    date = models.DateTimeField(auto_now=False , auto_now_add=True) 
  

   