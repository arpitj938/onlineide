from __future__ import unicode_literals

from django.db import models

class user_data(models.Model):
	user_no=models.AutoField(primary_key=True)
	user_id=models.CharField(max_length=120,blank=True,null=False)
	user_name=models.CharField(max_length=120,blank=True,null=True)
	email=models.CharField(max_length=120,blank=True,null=True)
	roll_no=models.DecimalField(max_digits=10,decimal_places=0,unique=True)
	sem=models.DecimalField(decimal_places=0, max_digits=2)
# Create your models here.
