# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django import forms

# Create your models here.

class Car(models.Model):
	car_id=models.CharField(max_length=50)
	lat=models.CharField(max_length=50)
	lang=models.CharField(max_length=50)
	#radius=models.CharField(max_length=50)
	start=models.DateTimeField(blank=True,null=True)
	end=models.DateTimeField(blank=True,null=True)
	def __unicode__(self):
		return "%s %s %s %s %s" %(self.car_id,self.lat, self.lang,self.start,self.end)


class Parking(models.Model):
	car_id=models.CharField(max_length=50,blank=True,null=True)
	parking_slot=models.CharField(max_length=200)
	availibility=models.IntegerField(blank=True,null=True)

	start=models.DateTimeField(blank=True,null=True)
	end=models.DateTimeField(blank=True,null=True)
	def __unicode__(self):
	
		return "%s %s %s %s %s" %(self.car_id, self.parking_slot,self.availibility,self.start,self.end)