from django.conf.urls import url
from . import views

app_name='parking'
urlpatterns=[

	url(r'^$',views.menu, name='menu'),
	url(r'^car/$',views.car, name='car'),
	url(r'^car_success/$',views.car_success, name='car_success'),

	url(r'^reserve/$',views.reserve, name='reserve'),
	url(r'^reserve_view/$',views.reserve_view, name='reserve_view'),
	url(r'^delete/$',views.delete, name='delete'),
	
	#url(r'^delete_reserve/$',views._reserve, name='_reserve'),
		
]