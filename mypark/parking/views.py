# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from .forms import CarForm

from django import forms

from .models import Car, Parking

from django.template import loader

from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.


def car(request):
	if request.method=='POST':
		form=CarForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/parking/car_success')
		else:
			return render(request,'car.html',{'form':form})
	form =CarForm()
	return render(request,'car.html',{'form':form})

def car_success(request):
	car=Car.objects.all()
	for s in car:
		print s.car_id
	parking=Parking.objects.filter(availality=1)

	print parking
	return render_to_response('car_success.html',{'car':car,'parking':parking})



