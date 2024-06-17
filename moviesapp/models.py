from django.db import models

class Show(models.Model):
    name = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()  # Assuming duration is in minutes
    rating = models.FloatField(choices=[(i / 2, i / 2) for i in range(1, 11)], default=0.0)
    year_of_release = models.PositiveIntegerField()
    studio = models.CharField(max_length=30)


    def __str__(self):
        return self.name

