from django.shortcuts import render, redirect, RequestContext
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from app.models import User

def is_valid_user(request):
    emailVar = request.POST.get('email')
    passwordVar = request.POST.get('password')

    user = User.objects.filter(email=emailVar, password=passwordVar).first()

    if not user:
        return HttpResponse("invalid")
    else:
        request.session['user_id'] = user.id
        request.session['user_type'] = user.user_type
        request.session['name'] = user.name

        return HttpResponse("correct")


def logout(request):

    del request.session['user_id']
    del request.session['user_type']
    del request.session['name']

    return redirect('/')

