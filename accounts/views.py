import uuid
import sys

from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.contrib import auth, messages

from django.urls import reverse
# from django.contrib.auth import login as auth_login, logout as auth_logout
# from django.contrib.auth import authenticate
from accounts.models import Token


# Create your views here.

def send_login_email(request):
    '''отправить сообщение для входа в систему'''
    email = request.POST['email']
    uid = str(uuid.uuid4())
    token = Token.objects.create(email=email)
    print('saving uid', uid, 'for email', email, file=sys.stderr)
    # url = request.build_absolute_uri(
    #     f'/accounts/login?=uid={uid}'
    # )
    url = request.build_absolute_uri(
        reverse('login') + '?token=' + str(token.uid)
    )
    print(type(send_mail))
    message_body = f"Use this link to log in:\n\n{url}"

    send_mail(
    'Your login link for Superlists',
    message_body,
    'noreply@superlists',
    [email],
    )
    messages.success(
        request,
        "Проверьте свою почту, мы отправили Вам ссылку, \
            которую можно использовать для входа на сайт."
    )
    return redirect('/')
    # return render(request, 'login_email_sent.html')


def login(request):
    """зарегистрировать вход в систему"""
    print('login view', file=sys.stderr)
    uid = request.GET.get('uid')
    # user = auth.authenticate(uid=uid)
    user = auth.authenticate(uid=request.GET.get("token"))

    auth.login(request, user)
    if user is not None:
        auth.login(request, user)
    return redirect('/')


def logout(request):
    """ выход из системы """
    auth.logout(request)
    return redirect('/')
