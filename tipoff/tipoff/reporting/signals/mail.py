# coding=utf-8
import smtplib

from django.db.models.signals import post_save
from django.dispatch import receiver
from reporting.models import IncidentReport
from django.core.mail import send_mail


@receiver(post_save, sender=IncidentReport)
def my_handler(instance, created, **kwargs):
    if created:
        print(" email processing ")
        send_mail('Fraud Report',
                  'An Anonymous Fraud report has been submitted in the Tipoff system. '
                  'Please logon http://127.0.0.1:8000 to view this Report',
                  'mukwazhi@gmail.com', ['mukwazhi@gmail.com', 'bmukwazhi@nhszim.com'])
        print(" email send ")
