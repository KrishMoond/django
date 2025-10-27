from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings

def send_email(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient = request.POST.get('recipient')
        attachment = request.FILES.get('attachment')

        # Create email
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient],
        )

        # Add attachment if provided
        if attachment:
            email.attach(attachment.name, attachment.read(), attachment.content_type)

        # Send email
        email.send(fail_silently=False)

        return render(request, 'email_sent.html')

    return render(request, 'send_email.html')
