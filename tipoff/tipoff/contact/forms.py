# coding=utf-8
from django import forms
from captcha.fields import CaptchaField


class ContactForm(forms.Form):
    captcha = CaptchaField()
    subject = forms.CharField(max_length=100)
    contact_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False)