from django.db import models
from django.db.models.base import Model

# Create your models here.
class UserInput(models.Model):
    Fixed_Acidity = models.CharField(max_length=20)
    Volatile_Acidity = models.CharField(max_length=20)
    Citric_Acid = models.CharField(max_length=20)
    Residual_Sugar = models.CharField(max_length=20)
    Chlorides = models.CharField(max_length=20)
    Free_SulphurDioxode = models.CharField(max_length=20)
    Total_SulphurDioxide = models.CharField(max_length=20)
    Density = models.CharField(max_length=20)
    pH = models.CharField(max_length=20)
    Sulphates = models.CharField(max_length=20)
    Alchohol = models.CharField(max_length=20)

    def __str__(self) -> str:
        return super().__str__()