from django.conf.urls import patterns, url, include

from LZ_graham import views


urlpatterns = patterns('',
	# ex: /LZ/graham/
	url(r'^$', views.index, name='index'),
	#url(r'^$', views.IndexView.as_view(), name='index'),
	
	# ex: /LZ/graham/%CLIENT_NAME%/
	#url(r'^(?P<client_name>[a-zA-Z]+)/$', views.client, name='client'),
	#url(r'^(?P<client_name>[^/]*)[&](?P<pwd>[^/]*)/$', views.client, name='client'),
	
	#url(r'^signin/', views.signin, name='signin'),
	url(r'^register/', views.register, name='register'),
	url(r'^login/', views.login, name='login'),
	#url(r'^login/(?P<status>[^/]*)/$', views.client, name='client'),
	url(r'^client/', views.client, name='client'),
)
