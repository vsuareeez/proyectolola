from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Details(models.Model):
    type = models.CharField(max_length=20,default='',null=False)
    name = models.CharField(max_length=30,default='',null=False)