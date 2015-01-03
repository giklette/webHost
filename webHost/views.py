from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404



def home(request):
	# return HttpResponse("<b>Hello, world</b>, you're at the home index.")

	context = {'mytext': 'salut les filles !' }
	return render(request, 'index.html', context)
	
