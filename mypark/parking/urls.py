from django.conf.urls import url
from parking import views

app_name='parking'
urlpatterns=[

	
	
	url(r'^car/$',views.car, name='car'),
	url(r'^car_success/$',views.car_success, name='car_success'),

	#url(r'^reverse/$',views.reverse, name='reserve'),
	#url(r'^view_reserve/$',views.view_reserve, name='view_reserve'),
	#url(r'^update_reserve/$',update_reserve, name='update_reserve'),
	
	#url(r'^delete_reserve/$',views._reserve, name='_reserve'),
		
]