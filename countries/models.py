from django.db import models

# Create your models here.
class Country(models.Model):
    name=models.CharField(max_length=100)
    capital=models.CharField(max_length=100)
    area=models.IntegerField()


class States(models.Model):
    name=models.CharField(max_length=200)
    country=models.ForeignKey(Country,on_delete=models.CASCADE)

    def __str__(self):
        return self.name