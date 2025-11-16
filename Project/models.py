from django.contrib import messages
from django.db import models

from django.shortcuts import redirect


class customer(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)

