from django.shortcuts import render, redirect, RequestContext
from django.http import HttpResponse
from django.contrib.sessions.models import Session

import json

from app.models import Project,Bug,BugUser,User

def user_section(request):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    running_projects = Project.objects.filter({'status': 'active'})
    closed_projects = Project.objects.filter({'status': 'closed'})
    current_bugs = Bug.objects.filter({'status': 'active'})
    fixed_bugs = Bug.objects.filter({'status': 'fixed'})
    unresolved_bugs = Bug.objects.filter({'status': 'unresolved'})

    user_bugs = BugUser.objects.filter({'user_id': user_id, 'status': 'active'})

    response_data = {
                        'running_projects': running_projects,
                        'closed_projects': closed_projects,
                        'current_bugs': current_bugs,
                        'fixed_bugs': fixed_bugs,
                        'unresolved_bugs': unresolved_bugs,
                        'user_bugs': user_bugs
                    }

    return render(request, 'users/user-section.html', response_data)


def create_user(request):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    return render(request, 'users/create.html')


def save_user(request):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"

    email = request.POST.get('email')

    user = User.objects.get({'email': email})

    if user:
        print('Duplicate email')
    else:
        user = User.new

        user.email = email
        user.name = request.POST.get('name')
        user.password = request.POST.get('password')
        user.user_type = request.POST.get('user_type')
        user.status = 'active'

        user.save()

        print('User created successfully')



def profile(request):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    user = User.objects.get(id=user_id)

    if user:
        return render(request, 'users/profile.html', {'user': user})
    else:
        return redirect('/')


def update_profile(request):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"

    user = User.objects.get(id=user_id)

    if user:

        email = request.POST.get('email')

        user_by_email = User.objects.get({'email': email})

        if user_by_email and (not(user_by_email.id == user_id)):
            print('Email already taken')
        else:
            user.email = email
            user.name = request.POST.get('name')
            user.password = request.POST.get('password')
            user.user_type = request.POST.get('user_type')

            user.save()

            print('Profile updated successfully')
    else:
        print('Invalid user')


def edit_user(request, user_id):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    if user_id:
        user = User.objects.get(id=user_id)

        request.session['current_edit_user'] = user_id

        if user:
            return render(request, 'users/edit.html', {'user': user})
        else:
            return redirect('/')

    else:
        return redirect('/')


def update_user(request):

    user_id = request.session['user_id']
    if not user_id:
        return "invalid"

    user = User.objects.get(id=user_id)

    if user:

        user.name = request.POST.get('name')
        user.password = request.POST.get('password')
        user.user_type = request.POST.get('user_type')

        user.save()

        print('Profile updated successfully')

    else:
        print('Invalid user')


def list_users(request):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    return render(request, 'users/list.html')


def remove_user(user_id):

    if user_id:

        user = User.objects.get(id=user_id)

        if user:
            user.status = 'removed'

            user.save()

            print('done')

        else:
            print('invalid')

    else:
        print('invalid')


#************** json methods ***************

def data_list_users(request):

    user_id = request.session['user_id']
    if not user_id:
        return HttpResponse(json.dumps({'message': 'not logged'}), content_type="application/json")

    users = User.objects.get({'status': 'active'})

    if users and len(users)>0:
        response_data = {'found': True, 'users': users, 'message': 'logged'}
    else:
        response_data = {'found': False, 'message': 'logged'}

    return HttpResponse(json.dumps(response_data), content_type="application/json")