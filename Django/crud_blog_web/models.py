from django.db import models


# Create your models here.
class Article(models.Model):
    # pole 150 znaków
    # Mogę stworzyć inny artykuł o tym samym tytule
    title = models.CharField(max_length=150, blank=False, unique=False)
    # Jeżeku nikt nie poda roku powstania artykułu to pole zostanie uzupełnione rokiem 2023
    year = models.PositiveSmallIntegerField(default=2023)


    def __str__(self):
        return self.title