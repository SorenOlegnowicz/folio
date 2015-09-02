from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from twilio.rest import TwilioRestClient


class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    message = models.CharField(max_length=1000)


client = TwilioRestClient()

@receiver(post_save, sender=Contact)
def create_sms(sender, instance, created=False, **kwargs):
    if created:
        print(instance.name)
        client.messages.create(to='+14344651523',
                               from_="+12513331231",
                               body= 'Name: ' + instance.name + '   Email: ' + instance.email + '   Message: ' + instance.message)