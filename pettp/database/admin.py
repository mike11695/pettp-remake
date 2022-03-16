from django.contrib import admin
from .models import Pet

# Register your models here.

#Define Pet Class
class PetAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'species', 'converted', 'user', 'verified')
    list_filter = ('color', 'species', 'converted', 'user', 'verified')

# Register pet model to admin class
admin.site.register(Pet, PetAdmin)
