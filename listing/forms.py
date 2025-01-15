from django import forms
from django.utils.text import slugify
from .models import Wanted


class WantedForm(forms.ModelForm):
    """
    Form for creating or editing a wanted listing

    The form allows user to enter
    pirate's name,
    bounty,
    description,
    status and upload an image
    """

    class Meta:
        model = Wanted
        fields = [
            'pirate_name',
            'bounty',
            'description',
            'status',
            'pirate_image']
    
    """
    This will generate a slug based on a pirates name
    """

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.slug = slugify(instance.pirate_name)
        if commit:
            instance.save()
        return instance
