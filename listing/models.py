from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField

STATUS = ((0, "At Large!"), (1, "Caught!"))


# Create your models here.
""" 
Details of pirate listed on wanted site  

Attributes: 
    pirate_name: Unique name of pirate
    slug: Unique identifier
    bounty: Value of pirate
    pirate_image: Image uploaded of pirate
    description: Description of reason why pirate is wanted
    created_on: Creation date and time of listing
    updated_on: Date and time listing has been updated
    status: The status if pirate is caught or at large
    author: User who created the listing
"""
class Wanted(models.Model):
    pirate_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    bounty = models.BigIntegerField(validators=[MinValueValidator(1)])
    pirate_image = CloudinaryField('image', default='')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="Marine"
    )

    """ Returns string representation of prate by name and bounty """
    def __str__(self):
        return f" {self.pirate_name} | Bounty: {self.bounty}"
    
    """ Formats the bounty to have commas for readability"""
    def formatted_bounty(self):
        return f"{self.bounty:,}"
