from django import forms
from django.utils.text import slugify
from .models import Wanted

class WantedForm(forms.ModelForm):
    class Meta:
        model = Wanted
        fields = ['pirate_name', 'bounty', 'description', 'status']

    def save(self, commit=True):
        # Auto-generate the slug based on pirate_name
        instance = super().save(commit=False)
        instance.slug = slugify(instance.pirate_name)
        if commit:
            instance.save()
        return instance