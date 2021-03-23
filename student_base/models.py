from django.db import models

class Words(models.Model):
    user_name = CharField(max_length=100, primary_key = True)
    word = CharField(max_length=50)
    translate = CharField(max_length=50)

