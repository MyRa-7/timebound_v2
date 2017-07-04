from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.
@python_2_unicode_compatible
class Profile(models.Model):
	name = models.CharField(max_length=25)
	user = models.OneToOneField(User, blank=True, null=True)

	def __str__(self):
		return self.name

@python_2_unicode_compatible
class Week(models.Model):
	week_number = models.IntegerField(default=0)
	parent_profile = models.ManyToManyField("Profile")

	def __str__(self):
		return '%s' %(self.week_number)

@python_2_unicode_compatible
class Thing(models.Model):
	parent_week = models.ManyToManyField ("Week")
	#models.OneToOneField(Week,on_delete=models.CASCADE,primary_key=False,)
	thing_name = models.CharField(max_length=25)
	thing_cost = models.IntegerField(default=0)
	#number_available = models.IntegerField(default=0)
	availability = models.BooleanField(default=True)
	photo = models.ImageField(upload_to='mythbala/', null=True)

	def __str__(self):
		return self.thing_name
