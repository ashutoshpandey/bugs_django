from django.shortcuts import render, redirect, RequestContext
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from app.models import User

def is_valid_user(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    user = User.objects.filter(email=email, password=password).first()

    if not user:
        return "invalid"
    else:
        request.session['userId'] = user.id
        request.session['userType'] = user.user_type
        request.session['name'] = user.name

        return "correct"


def logout(request):

    del request.session['userId']
    del request.session['userType']
    del request.session['name']

    return redirect('/app/')

