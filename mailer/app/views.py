from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient = request.POST.get('recipient')

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [recipient],
            fail_silently=False,
        )
        return render(request, 'email_sent.html')

    return render(request, 'send_email.html')
