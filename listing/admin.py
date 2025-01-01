from django.contrib import admin
from .models import Wanted
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Wanted)
class WantedAdmin(SummernoteModelAdmin):
    list_display = ('pirate_name', 'status', 'created_on', 'slug')
    search_fields = ['pirate_name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('pirate_name',)}
    summernote_fields = ('description',)


# Register your models here.
