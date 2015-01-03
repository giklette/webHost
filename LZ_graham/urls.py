from django.conf.urls import patterns, url

from LZ_graham import views

# from dajaxice.core import dajaxice_autodiscover, dajaxice_config
# dajaxice_autodiscover()

urlpatterns = patterns('',
	# ex: /LZ/graham/
	url(r'^$', views.index, name='index'),
	#url(r'^$', views.IndexView.as_view(), name='index'),
	
	# ex: /LZ/graham/%CLIENT_NAME%/
	#url(r'^(?P<client_name>[a-zA-Z]+)/$', views.client, name='client'),
	url(r'^(?P<client_name>[^/]*)[&](?P<pwd>[^/]*)/$', views.client, name='client'),
	
	# url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)
