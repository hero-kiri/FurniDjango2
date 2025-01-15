from django.core.mail import send_mail
from django.conf import settings

def send_code_email(user):
    subject = 'Регистрация на сайте Furni'
    message = 'Ваш код для подтверждения: ' + user.auth_code
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]
    send_mail(subject, message, email_from, recipient_list)
    print('Email sent to:', user.email, 'with code:', user.auth_code)