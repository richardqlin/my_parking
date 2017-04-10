# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

from .forms import SpotsForm

from django import forms

from .models import Spots, Paking

from django.template import loader

from django.http import HttpResponse, Http404, HttpResponseRedirect

# Create your views here.


def spots(request):
	if request.method=='POST':
		form=SpotsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/paking/spots_success')
		else:
			return render(request,'spots.html',{'form':form})
	form =SpotsForm()
	return render(request,'spots.html',{'form':form})

def spots_success(request):
	spot=Spots.objects.all()
	return render_to_response('spots_success.html',{'spot':spot})



