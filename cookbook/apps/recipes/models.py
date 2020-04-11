from django.db import models
# from django.contrib.auth.models import User

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    time_category = models.CharField(max_length=100)
    recipe_detail = models.CharField(max_length=1000, blank=True, null=True)
    # owner = models.ForeignKey(User, related_name="recipes", on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name
