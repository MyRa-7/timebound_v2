from django.contrib import admin

# Register your models here.
from .models import Week, Thing

admin.site.register(Week)
admin.site.register(Thing)