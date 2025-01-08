from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "At Large!"), (1, "Caught!"))

# Create your models here.
class Wanted(models.Model):
    pirate_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    bounty = models.IntegerField()
    pirate_image = CloudinaryField('image', default='placeholder')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Marine"
    )

    def __str__(self):
        return f" {self.pirate_name} | Bounty: {self.bounty}"

   