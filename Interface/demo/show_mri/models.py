from django.db import models

# Create your models here.

class Patient(models.Model):
	patient_id = models.CharField(max_length=10)
	MGMT_type = models.IntegerField()
	FLAIR_imgc = models.IntegerField()
	T1w_imgc = models.IntegerField()
	T2w_imgc = models.IntegerField()
	T1wCE_imgc = models.IntegerField()
