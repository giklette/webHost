# -*- coding: utf8 -*-

from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import RequestContext, loader
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse

from django.views import generic


from LZ_graham.models import Client


def index(request):
	''' # version base
	return HttpResponse("<b>Hello, world</b>, you're at the LZ/graham index.")
	'''

	''' # version simple (html en dur)
	client_list = Client.objects.all()
	output = ', '.join([p.client_name for p in client_list])
	return HttpResponse(output)
	'''
	
	''' # version template
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
	})
	return HttpResponse(template.render(context))
	'''

	''' # version template + render (meme resultat que version template)
	client_list = Client.objects.all()
	context = {'client_list': client_list}
	return render(request, 'LZ_graham/index.html', context)
	'''

	return render(request, 'LZ_graham/index.html')


def register(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	email = request.POST.get('email', '')
	
	if username == '' and password == '' and email == '':
		# ouverture de la page register.html
		context = {'result': 0}
	elif username == '':
		context = {'result': -1, 'email':email}
	elif email == '':
		context = {'result': -2, 'username':username}
	else:
		# tester si le username & email sont déjà présent dans la base de données ?
		
		# sinon :
		context = {'result': 0, 'username':username}
		return render(request, 'LZ_graham/login.html', context)
		
	return render(request, 'LZ_graham/register.html', context)

	
def login(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	
	if username == '':
		# ouverture de la page login.html
		context = {'result': 0}
	else:
		try:
			client = Client.objects.get(client_name = username)
			
			if client.password == password:
				# OK, on continue sur client.html
				context = {'client': client}
				return render(request, 'LZ_graham/client.html', context)
			else:
				# mot de passe incorrect
				context = {'result': -1, 'username':username}

		except Client.DoesNotExist:
			# client introuvable
			#raise Http404
			context = {'result': -2}

	return render(request, 'LZ_graham/login.html', context)
		
	'''
	username = request.POST.get('username', '')
	pwd = request.POST.get('password', '')
	
	try:
		client = Client.objects.get(client_name=username)
		
		if client.password == pwd:
			context = {'result': 1, 'client': client}
		else:
			context = {'result': -1, 'client': None}

	except Client.DoesNotExist:
		#raise Http404
		context = {'result': -2, 'client': None}
		
	return render(request, 'LZ_graham/client.html', context)
	'''

	
def client(request):
	return HttpResponse("TODO : <b>client</b> page")
	
	
def client_param(request, client_name, pwd):
	''' # version base
	return HttpResponse("You're looking at client %s." % client_name)
	'''

	try:
		client = Client.objects.get(client_name=client_name)
		
		if client.password == pwd:
			context = {'result': 0, 'client': client}
		else:
			context = {'result': 1, 'client': None}

	except Client.DoesNotExist:
		#raise Http404
		context = {'result': 2, 'client': None}
		
	return render(request, 'LZ_graham/client.html', context)