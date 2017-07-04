from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Week(models.Model):
	week_number = models.IntegerField(primary_key=True)

	def __str__(self):
		return '%s' %(self.week_number)

@python_2_unicode_compatible
class Thing(models.Model):
	parent_week = models.ManyToManyField ("Week")
	#models.OneToOneField(Week,on_delete=models.CASCADE,primary_key=False,)
	thing_name = models.CharField(primary_key=True, max_length=25)
	thing_cost = models.IntegerField(default=0)
	#number_available = models.IntegerField(default=0)
	availability = models.BooleanField(default=True)

	def __str__(self):
		return self.thing_name
