from django.db import models

class Students(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    taken_class = models.CharField(max_length=200)

    def __str__(self):
        return self.name
