webHost
=======

références :
	https://docs.djangoproject.com/fr/1.7/
	http://openclassrooms.com/courses/developpez-votre-site-web-avec-le-framework-django
	
	http://www.dajaxproject.com/
	https://github.com/seawaywen/django-dajaxice
	https://github.com/seawaywen/django-dajax
	https://github.com/yceruto/django-ajax				???
	
	http://tutos-django.com/2012/03/04/un-formulaire-sexy-en-ajax/
	
	
	
	http://openclassrooms.com/courses/colorer-son-code-dans-une-balise-textarea-grace-a-javascript
	
---------------------------------------	
Hey All,

So the semester begins on Monday, meaning this whole week our department has been dealing with semester startup.  Making sure all our apps are tested, available, and production ready.  One of my apps has become the guinea pig for moving our infrastructure into the cloud.  This has been a really fun experience like rewriting parts to save to S3 instead of the filesystem, etc.  Except when it hasn’t been fun.  Like dealing with oAuth behind a load balancer.

Long story short, if you use Django, AWS, and oAuth or LTIs (and SSL), add this to your config file:

USE_X_FORWARDED_HOST = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

Basically, we have our website serving HTTPS through a load balancer, and due to some other infrastructure setup, our oAuth URL was being changed during the signature check.  This caused it to become invalid.  Adding the two lines above fix the whole issue.

Have a good weekend!

-Shea
---------------------------------------


http://lechaplinstlambert.cotecine.fr/horaires/
http://lechaplinstlambert.cotecine.fr/horaires/semaine-prochaine/