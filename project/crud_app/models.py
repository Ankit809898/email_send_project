from django.db import models


class Email(models.Model):
    fname = models.CharField(max_length=60)
    mname = models.CharField(max_length=60)
    lname = models.CharField(max_length=60)
    gender = models.CharField(max_length=60)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    attach = models.FileField()
    message = models.CharField(max_length=1000)