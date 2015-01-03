from django.conf.urls import include, url
from django.contrib import admin
#from django.views.generic.base import RedirectView

urlpatterns = [
	# Examples:
	url(r'^$', 'webHost.views.home', name='home'),
	url(r'^admin/', include(admin.site.urls)),
		
	# url(r'^blog/', include('blog.urls')),
	# url(r'^polls/', include('polls.urls')),
	url(r'^polls/', include('polls.urls', namespace="polls")),
	
	url(r'^LZ/', include('LZ_graham.urls', namespace="LZ_graham")),
	url(r'^LZ/graham/', include('LZ_graham.urls', namespace="LZ_graham")),  
]
