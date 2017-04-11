# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from .forms import CarForm, ParkingForm
from datetime import datetime
from django import forms

from .models import Car, Parking

from django.template import loader

from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.


def menu(request):
	time=datetime.now()
	return render(request,'menu.html',{'time':time})


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
		a= s.car_id
		a=str(a)
		car_start=s.start
		car_end=s.end
		break

 
	parking=Parking.objects.all()
	print parking
	for p in parking: 
	
		print p
		if p.availibility==1:
			p.availibility=0
			p.car_id=a
			p.start=car_start
			p.end=car_end
			p.save()
		
			break

	return render_to_response('car_success.html',{'car':car,'parking':parking})


def reserve(request):
	
	if request.method=='POST':
		p_form=ParkingForm(request.POST)
		if p_form.is_valid():
			p_form.save()
			return HttpResponseRedirect('/parking/reserve_view')
		else:
			return render(request,'reserve.html',{'p_form':p_form})
	p_form =ParkingForm()
	return render(request,'reserve.html',{'p_form':p_form})


def reserve_view(request):
	park=Parking.objects.all()
	return render(request,'reserve_view.html',{'park':park})

def delete(request):
	parking=Parking.objects.all()
	query=request.GET.get('q')
	if query:
		print query
		parking_exist=parking.filter(pk=query)
		if parking_exist.count()>0:
			parking=parking.get(pk=query)
			parking.delete()
	

	return render(request,'delete.html',{'parking':parking})
