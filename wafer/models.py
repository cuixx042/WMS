from django.db import models
from django.contrib.auth.models import AbstractUser

from django.urls import reverse

from imagekit.models import ProcessedImageField

# Create your models here.

class Account(models.Model):
	title = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.title

class WaferUser(AbstractUser):
	first_name = models.CharField(max_length=20, blank=True, null=True)
	last_name = models.CharField(max_length=20, blank=True, null=True)
	# account = models.ForeignKey(
	# 	Account,
	# 	on_delete=models.CASCADE,
	# 	related_name='account_wafers',
	# )
	profile_pic = ProcessedImageField(
		upload_to='static/images/profiles',
		format='JPEG',
		options={'quality': 100},
		null=True,
		blank=True,
		)

	def get_absolute_url(self):
		return reverse('user_detail', args=[str(self.pk)])

	def __str__(self):
		return self.username

class Customer(models.Model):
	title = models.CharField(max_length=20, blank=True, null=True)

	def __str__(self):
		return self.title

class Wafer(models.Model):
	title = models.CharField(max_length=20, blank=True, null=True)
	project = models.CharField(max_length=20, blank=True, null=True)

	owner = models.ForeignKey(
		WaferUser,
		on_delete=models.CASCADE,
		related_name='user_wafers',
	)
	ctm = models.ForeignKey(
		WaferUser,
		on_delete=models.CASCADE,
		related_name='ctm_wafers',
	)
	account = models.ForeignKey(
		Account,
		on_delete=models.CASCADE,
		related_name='account_wafers',
	)
	customer = models.ForeignKey(
		Customer,
		on_delete=models.CASCADE,
		related_name='customer_wafers',
	)

	in_time = models.DateField(editable=True)
	out_time = models.DateField(editable=True)
	image = ProcessedImageField(
		upload_to='static/images/wafers',
		format='JPEG',
		options={'quality':100},
		blank=True, 
		null=True,
	)
	notes = models.TextField(blank=True, null=True)

	posted_on = models.DateTimeField(auto_now_add=True, editable=False)

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("wafer_detail", args=[str(self.pk)])	