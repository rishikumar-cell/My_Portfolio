from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from threading import Thread
import logging
from django.core.mail import EmailMessage

# Set up logger
logger = logging.getLogger(__name__)

def send_email_async(subject, message, from_email, recipient_list, reply_to=None):
    """
    Sends email asynchronously using a thread.
    Adds Reply-To header if provided.
    """
    def send():
        try:
            email = EmailMessage(
                subject=subject,
                body=message,
                from_email=from_email,
                to=recipient_list,
                headers={'Reply-To': reply_to} if reply_to else None
            )
            email.send(fail_silently=False)
            logger.info("Email sent successfully via SendGrid")
        except Exception as e:
            logger.error(f"Email sending failed: {e}")
    Thread(target=send).start()

def index(request):
    """
    Renders the home/contact page and handles form submissions.
    Sends emails asynchronously using SendGrid SMTP to avoid blocking the request.
    """
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        # Validate form fields
        if not all([name, email, message_text]):
            messages.error(request, "Please fill in all fields.")
            return redirect('index')

        # Prepare email content
        subject = f"New Message From {name} <{email}>"
        full_message = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message_text}"

        # Send email asynchronously with Reply-To
        send_email_async(
            subject,
            full_message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.DEFAULT_FROM_EMAIL],  # Receiving email (your inbox)
            reply_to=email                  # Replies go to sender
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('index')

    # Render the home/contact page
    return render(request, 'index.html')
