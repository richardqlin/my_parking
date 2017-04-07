# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from .forms import SpotsForm

from django import forms

from .models import Spots, Paking

from django.template import loader


# Create your views here.


def spots(request):
	if request.method=='POST':
		form=SpotsForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/spots/success')
		else:
			return render(request,'location.html',{'form':form})
	form =SpotsForm()
	return render(request,'location.html',{'form':form})





