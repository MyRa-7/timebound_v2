from django.contrib import admin

# Register your models here.
from .models import Week, Thing, Profile

admin.site.register(Week)
admin.site.register(Thing)
admin.site.register(Profile)