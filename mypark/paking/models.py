# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django import forms

# Create your models here.

class Spots(models.Model):
	spots=models.CharField(max_length=50)
	lat=models.CharField(max_length=50)
	lang=models.CharField(max_length=50)
	#radius=models.CharField(max_length=50)
	parkingtime=models.DateTimeField(blank=True,null=True)

	def __unicode__(self):
		return "%s %s %s %s" %(self.spots,self.lat, self.lang,self.parkingtime)


class Paking(models.Model):
	paking=models.CharField(max_length=200)
	availality=models.IntegerField(blank=True,null=True)
	#expiretime=models.DateTimeField(db_column='expireTime', blank=True,null=True)

	def __unicode__(self):
		managed=True
		return self.paking