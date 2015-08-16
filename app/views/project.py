from django.shortcuts import render, redirect, RequestContext
from django.http import HttpResponse
from django.contrib.sessions.models import Session

import json

from app.models import Project

def create_project(request):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    return render(request, 'projects/create.html')


def save_project(request):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"

    name = request.POST.get('name')
    project = Project.objects.filter({'name': name, 'status': 'active'})

    if project:
        return "duplicate"
    else:
        project = Project.new

        project.name = name
        project.description = request.POST.get('description')
        project.status = 'active'
        project.created_by = request.session['user_id']

        project.save()

        print('done')



def edit_project(request, project_id):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    project = Project.objects.get(id=project_id)

    request.session['currentProjectId'] = project_id

    return render(request, 'projects/edit.html', {'project': project})


def update_project(request):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"

    project_id = request.session['current_project_id']

    project = Project.objects.get(id=project_id)

    if project:

        name = request.POST.get('name')
        description = request.POST.get('description')
        status = request.POST.get('status')

        if name:
            project.name = request.POST.get('name')

        if description:
            project.description = request.POST.get('description')

        if status:
            project.status = request.POST.get('status')

        project.save()

        print('done')

    else:
        print('invalid')


def remove_project(request, project_id):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"

    if id:

        project = Project.objects.get(id=project_id)

        if project:
            project.status = 'removed'

            project.save()

            #Bug::where('project_id', '=', id).update(array('status' => 'removed'))

            print('done')

        else:
            print('invalid')

    else:
        print('invalid')


def list_projects(request):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    projects = Project.objects.filter('status','active')

    return render(request, 'projects/list.html', {'projects': projects})


#***************** json methods *****************
def data_list_projects(request):

    user_id = request.session['user_id']
    if not user_id:
        return HttpResponse(json.dumps({'message': 'not logged'}), content_type="application/json")

    projects = Project.objects.filter({'status','active'})

    if projects and len(projects)>0:
        response_data = {'found': True, 'projects': projects, 'message': 'logged'}
    else:
        response_data = {'found': False, 'message': 'logged'}

    return HttpResponse(json.dumps(response_data), content_type="application/json")