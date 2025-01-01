from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Wanted(models.Model):
    pirate_name = models.CharField(max_length=200, unique=True)
    bounty = models.IntegerField()
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Marine"
    )

    def __str__(self):
        return f" {self.pirate_name} | Bounty: {self.bounty}"

