from django.db import models

# Create your models here.


class Client(models.Model):
	FREE = "free"
	ORANGE = "orange"
	SFR = "sfr"
	BOUYGUE = "bouygue"
	
	APN_CHOICES = (
		(FREE, "Free Mobile"),
		(ORANGE, "Orange"),
		(SFR, "SFR"),
		(BOUYGUE, "Bouygue Telecom"),
	)
	
	client_name = models.CharField(max_length=30)
	password = models.CharField(max_length=30)
	creation_date = models.DateTimeField('date created')
	phone_number = models.CharField(max_length=12)
	unlock_PIN_code = models.PositiveSmallIntegerField()
	APN_name = models.CharField(max_length=20, choices=APN_CHOICES, default=FREE)
	APN_username = models.CharField(max_length=30)
	APN_password = models.CharField(max_length=30)
	message_phone = models.CharField(max_length=2000)
	receivers_phone = models.CharField(max_length=12)

	use_email_confirmaton = models.BooleanField(default=True)
	object_email = models.CharField(max_length=100)
	receivers_email = models.EmailField(max_length=100)
	
	#def __str__(self):			# python 3
	def __unicode__(self):		# python 2
		return self.client_name

