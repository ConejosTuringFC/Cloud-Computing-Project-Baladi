from django.db import models
# Create your models here.

class Flux(models.Model):
	date_time = models.DateTimeField("Date published")
	flux = models.DecimalField(max_digits=10, decimal_places=5)

