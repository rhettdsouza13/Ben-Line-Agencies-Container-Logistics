from django.db import models
import os
# Create your models here.
class ContainerIn(models.Model):
    def __str__(self):
        return self.CONTAINER_NO
    VSL_NAME = models.CharField(max_length=200)
    VOY_NUMBER = models.CharField(max_length=200)
    CONTAINER_NO = models.CharField(max_length=200)
    TERMINAL = models.CharField(max_length=200, null=True, blank=True)
    ACCOUNT = models.CharField(max_length=200, null=True, blank=True)
    SIZE = models.CharField(max_length=50, null=True, blank=True)
    STATUS = models.CharField(max_length=50)
    ICD_LOCAL = models.CharField(max_length=50)
    POD = models.CharField(max_length=200, null=True, blank=True)
    DISCHARGE_DATE = models.CharField(max_length=50, null=True, blank=True)
    RAIL_ROUND_OUT = models.CharField(max_length=50, null=True, blank=True)
    EMPTY_IN = models.CharField(max_length=200, null=True, blank=True)
    YARD = models.CharField(max_length=200, null=True, blank=True)
    REMARKS = models.CharField(max_length=2000, null=True, blank=True)

class Documents(models.Model):
    def __str__(self):
        return os.path.basename(self.excel.name)
    excel = models.FileField(upload_to='documents/%d')
