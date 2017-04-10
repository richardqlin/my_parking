from django.conf.urls import url
from paking import views

app_name='paking'
urlpatterns=[

	
	
	url(r'^spots/$',views.spots, name='spots'),
	url(r'^spots_success/$',views.spots_success, name='spots_success'),

	#url(r'^reverse/$',views.reverse, name='reserve'),
	#url(r'^view_reserve/$',views.view_reserve, name='view_reserve'),
	#url(r'^update_reserve/$',update_reserve, name='update_reserve'),
	
	#url(r'^delete_reserve/$',views._reserve, name='_reserve'),
		
]