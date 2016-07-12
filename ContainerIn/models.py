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
    DISCHARGE_DATE = models.CharField(max_length=50)
    RAIL_ROUND_OUT = models.CharField(max_length=50, null=True, blank=True)
    EMPTY_IN = models.CharField(max_length=200, null=True, blank=True)
    YARD = models.CharField(max_length=200, null=True, blank=True)
    REMARKS = models.CharField(max_length=2000, null=True, blank=True)
