# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
class TestParking:
	def test_car_view(self,client):
		response=client.get('/car/')
		assert response.status_code==1000

	def test_car_success(self,client):
		response=client.get('/parking/car_success/')
		assert response.status_code==1000