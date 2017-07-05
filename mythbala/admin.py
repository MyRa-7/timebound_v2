from django.contrib import admin

# Register your models here.
from .models import Week, Thing, Profile

# class WeekInline(admin.StackedInline):
# 	model = Week
# 	extra = 1

# class ProfileAdmin(admin.ModelAdmin):
# 	fieldsets = [
# 		(None,	{'fields': ['name']}),
# 	]
# 	inlines = [WeekInline]
#	changing a bit to ensure another commit
		
admin.site.register(Profile)
admin.site.register(Week)
admin.site.register(Thing)