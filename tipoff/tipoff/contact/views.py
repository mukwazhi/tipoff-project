from django.shortcuts import render
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            contact_email = form.cleaned_data['contact_email']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['bmukwazhi@nhszim.com']
            if cc_myself:
                recipients.append(contact_email)

            if subject and message and contact_email and recipients:
                try:
                    print(recipients)
                    send_mail(subject, message, contact_email, recipients)
                    print("ok1")
                except BadHeaderError:
                    return HttpResponse('Invalid header found.')
                return HttpResponseRedirect('/contact/thanks/')
        else:
            form = ContactForm()
            #return HttpResponse('Make sure all fields are entered and valid.')
    else:
        form = ContactForm()

    context = {
        'form': form,
    }
    template = 'contact.html'

    return render(request, template, context)
