from django.db import models


class Review(models.Model):
    tour = models.ForeignKey('tours.TourPackage', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return f"Review by {self.author}"


class Rating(models.Model):
    tour = models.ForeignKey('tours.TourPackage', on_delete=models.CASCADE)
    stars = models.IntegerField()

    def __str__(self):
        return f"{self.stars} stars"
