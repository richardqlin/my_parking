# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django import forms

# Create your models here.

class Spots(models.Model):
	spots=models.CharField(max_length=50)
	lat=models.CharField(max_length=50)
	lang=models.CharField(max_length=50)
	radius=models.CharField(max_length=50)
	timer=models.CharField(max_length=50)

	def __unicode__(self):
		return "%s %s %s " %(self.spots,self.lat, self.lang)


class Paking(models.Model):
	paking=models.ForeignKey(Spots,on_delete=models.CASCADE)
	parking_time=models.CharField(max_length=50)

	def __unicode__(self):
		return self.paking