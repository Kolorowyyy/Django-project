from django.db import models

# Create your models here.
class TourPackage(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.IntegerField()
    start_date = models.DateField()

    def __str__(self):
        return self.title