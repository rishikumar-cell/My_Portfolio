from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from threading import Thread

# Async email sender
def send_email_async(subject, message, from_email, recipient_list):
    Thread(
        target=send_mail,
        args=(subject, message, from_email, recipient_list),
        kwargs={'fail_silently': False}
    ).start()

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        if name and email and message_text:
            subject = f"New Message From {name} <{email}>"
            full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}"

            try:
                send_email_async(
                    subject,
                    full_message,
                    settings.EMAIL_HOST_USER,
                    [settings.EMAIL_HOST_USER]  # Your receiving email
                )
                messages.success(request, "Your message has been sent successfully!")
            except Exception as e:
                messages.error(request, f"Error sending message: {e}")
        else:
            messages.error(request, "Please fill in all fields.")

        return redirect('index')  # Avoid resubmission

    return render(request, 'index.html')
