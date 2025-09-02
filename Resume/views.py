from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email  = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            subject = f"New Message From {name} <{email}>"  # <-- subject shows sender's name & email
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        
            try:
                send_mail(
                    subject,                     # This is what shows in inbox
                    full_message,
                    settings.EMAIL_HOST_USER,    # From
                    [settings.EMAIL_HOST_USER],  # To (your Gmail)
                    fail_silently=False,
                )
                messages.success(request, "Your message has been sent successfully")
            except Exception as e:
                messages.error(request, f"Error sending message: {e}")
        else:
            messages.error(request, "Please fill in all fields")
        return redirect('index')  # redirect to avoid resubmission

    return render(request, 'index.html')
