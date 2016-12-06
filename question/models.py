from __future__ import unicode_literals

from django.db import models

class question_data(models.Model):
	q_id=models.AutoField(primary_key=True)
	q_name=models.CharField(max_length=120,blank=True,null=True)
	q_question=models.TextField(blank=True,null=True)
	q_type=models.CharField(max_length=120,blank=True,null=True)
	q_max_time=models.TimeField()
	q_max_memory=models.DecimalField(decimal_places=0, max_digits=10)

# Create your models here.
