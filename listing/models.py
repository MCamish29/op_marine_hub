from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wanted(models.Model):
    pirate_name = models.CharField(max_length=200, unique=True)
    bounty = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Marine"
    )
