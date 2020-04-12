from django.db import models
from django.contrib.auth.models import User

class Timing(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Recipe(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, related_name="recipes_owned", on_delete=models.CASCADE, null=True)
    timing = models.ForeignKey(Timing, related_name='categories',on_delete=models.CASCADE)
    detail = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.name
