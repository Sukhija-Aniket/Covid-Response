from django.contrib import admin
from .models import Check

# Register your models here.
class CheckAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_severe', 'other_symptoms']

admin.site.register(Check, CheckAdmin)
