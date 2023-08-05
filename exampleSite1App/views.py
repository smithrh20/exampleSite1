from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import contactForm
from django.core.mail import send_mail, get_connection, EmailMessage
from django.conf import settings


#def homeView (request):
    #return render (request, 'home.html')

def homeView(request):
    submitted = False
    if request.method =='POST':
        form = contactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            #assert False
            con = get_connection('django.core.mail.backends.smtp.EmailBackend')
            #send_mail(
                #cd['subject'],
                #cd['message'],
                #cd.get('email', 'noreply@example.com'),
                #['smithrh20@gmail.com'],
                #connection=con

            email = EmailMessage(
                subject = ['subject'],
                body = ['message'],
                from_email = settings.EMAIL_HOST_USER,
                to = ['smithrh20@gmail.com'],
                reply_to = ['email'],
                )
                
            email.send()
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = contactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render (request, 'index.html', {'form':form, 'submitted': submitted})