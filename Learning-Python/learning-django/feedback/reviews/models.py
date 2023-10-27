from django.db import models

# Create your models here.


class Reviw(models.Model):
    user_name = models.CharField(max_length=100)
    review_text = models.TextField()
    rating = models.IntegerField()
