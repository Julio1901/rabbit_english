from django.db import models

class Words(models.Model):
    user_name = models.CharField(max_length=100)
    word = models.CharField(max_length=50)
    translate = models.CharField(max_length=50)

