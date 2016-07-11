from django.db import models

# Create your models here.
class ContainerIn(models.Model):
    def __str__(self):
        return self.CONTAINER_NO
    VSL_NAME = models.CharField(max_length=200)
    VOY_NUMBER = models.CharField(max_length=200)
    CONTAINER_NO = models.CharField(max_length=200)
    TERMINAL = models.CharField(max_length=200)
    ACCOUNT = models.CharField(max_length=200)
    SIZE = models.CharField(max_length=50)
    STATUS = models.CharField(max_length=100)
    POD = models.CharField(max_length=200)
    DISCHARGE_DATE = models.DateTimeField()
    RAIL_ROUND_OUT = models.DateTimeField()
    EMPTY_IN = models.CharField(max_length=200)
    YARD = models.CharField(max_length=200)
    REMARKS = models.CharField(max_length=2000)
