from django.shortcuts import render, redirect, RequestContext
from django.http import HttpResponse
from django.contrib.sessions.models import Session

import json
import time
import uuid

from app.models import User
from app.models import Bug
from app.models import BugComment
from app.models import BugCommentFile
from app.models import BugFile
from app.models import BugUser
from app.models import Project

def create_bug(request):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    project_id = request.session['currentProject']

    users = User.objects.all()

    if project_id:
        data = {'project_id': project_id, 'users': users}

        return render(request, 'bugs/create.html', data)
    else:
        return redirect('/')


def save_bug(request):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"


    bug = Bug.new

    bug.title = request.POST.get('title')
    bug.description = request.POST.get('description')
    bug.severity = request.POST.get('severity')
    bug.created_by = request.session['user_id']
    bug.project_id = request.session['currentProject']
    bug.status = 'active'

    bug.save()

    files = request.FILES.get('file')
    if files:
        fileCount = len(files)
    else:
        fileCount = 0

    users = request.POST.get('users')

    if users:
        userCount = len(users)
    else:
        userCount = 0

    if fileCount>0:
        for file in files:
            destinationPath = 'public/uploads'

            savedFileName = uuid.uuid4()

            filename = file.getClientOriginalName()
            file.move(destinationPath, savedFileName)

            bugFile = BugFile.new

            bugFile.bug_id = bug.id
            bugFile.file_name = filename
            bugFile.saved_file_name = savedFileName
            bugFile.status = 'active'

            bugFile.save()


    if userCount>0:

        for user_id in users:
            bug_user = BugUser.new

            bug_user.bug_id = bug.id
            bug_user.user_id = user_id
            bug_user.status = 'active'

            bug_user.save()

            user = User.objects.get(id=user_id)
            project = Project.objects.get(id=bug.project_id)

            if user:
                send_new_bug_email(user.name, user.email, project.name, bug.title, bug.description, None)


    print('done')


def edit_bug(request,id):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    bug = Bug.objects.find(id=id)

    return render(request, 'bugs/edit.html', {'bug':bug})


def update_bug(request):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"

    id = request.POST.get('id')

    bug = Bug.objects.find(id=id)

    if bug:

        title = request.POST.get('title')
        description = request.POST.get('description')
        status = request.POST.get('status')

        if title:
            bug.title = request.POST.get('title')

        if description:
            bug.description = request.POST.get('description')

        if status:
            bug.status = request.POST.get('status')

        bug.save()

        print('done')

    else:
        print('invalid')


def change_bug_status(request):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"

    id = request.POST.get('id')

    bug = Bug.objects.get(id=id)

    if bug:

        status = request.POST.get('status')

        if status:
            bug.status = status
            bug.save()

            print('done')

        else:
            print('invalid')

    else:
        print('invalid')


def list_bugs(request,project_id):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    if project_id:

        request.session['currentProject'] = project_id

        return render(request, 'bugs/list.html')
    else:
        return redirect('/')


def save_bug_comment(request):

    user_id = request.session['user_id']
    if not user_id:
        return "not logged"

    bug_comment = BugComment.new

    bug_comment.comment= request.POST.get('comment')
    bug_comment.created_by = request.session['user_id']
    bug_comment.bug_id = request.session['currentbug_id']
    bug_comment.status = 'active'

    bug_comment.save()

    files = request.FILES.get('file')
    fileCount = len(files)

    if fileCount>0:
        for file in files:
            destination_path = 'public/uploads'

            current_time = time.localtime(time.time())

            savedFileName = uuid.uuid4()

            filename = file.getClientOriginalName()
            file.move(destination_path, savedFileName)

            bug_comment_file = bug_comment_file.new

            bug_comment_file.bug_comment_id = bug_comment.id
            bug_comment_file.file_name = filename
            bug_comment_file.saved_file_name = savedFileName
            bug_comment_file.status = 'active'

            bug_comment_file.save()

    print('done')


def bug_detail(request,bug_id):

    user_id = request.session['user_id']
    if not user_id:
        return redirect('/')

    if bug_id:

        bug = Bug.objects.get(id=bug_id)
        project = Project.objects.get(id=bug.project_id)

        if bug and project:
            request.session['current_bug_id'] = bug_id

            bug_files = BugFile.objects.filter('bug_id', bug_id)

            data = {'project': project, 'bug': bug, 'bugFiles': bug_files}

            return render(request, 'bugs/detail.html', data)
        else:
            return redirect('/')
    else:
        return redirect('/')


def download_bug(bug_id):

    if bug_id:

        bug = Bug.objects.get(id=bug_id)

        if bug:

            bug_files = BugFile.objects.filter('bug_id', bug_id)

            if bug_files:

                for bug_file in bug_files:
                    x=5






#****************** json methods ***********************

def data_list_bugs(request):

    user_id = request.session['user_id']
    if not user_id:
        response_data = {'message': 'not logged'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    project_id = request.session['currentProject']

    bug_type = request.POST.get('bug_type')

    if project_id:
        bugs = Bug.objects.filter('project_id', project_id).where('status','=',bug_type).get()

        if bugs and len(bugs)>0:
            response_data = {'found': True, 'bugs': bugs, 'message': 'logged'}
        else:
            response_data = {'found': False, 'message': 'logged'}

    else:
        response_data = {'found': False, 'message': 'logged'}

    return HttpResponse(json.dumps(response_data), content_type="application/json")


def data_list_bug_comments(request):

    user_id = request.session['user_id']
    if not user_id:
        response_data = {'message': 'not logged'}
        return HttpResponse(json.dumps(response_data), content_type="application/json")

    bug_id = request.session['current_bug_id']

    if bug_id:
        comments = BugComment.objects.filter('bug_id', bug_id)

        if comments and len(comments)>0:
            response_data = {'found': True, 'comments': comments, 'message': 'logged'}
        else:
            response_data = {'found': False, 'message': 'logged'}
    else:
        response_data = {'found': False, 'message': 'logged'}

    return HttpResponse(json.dumps(response_data), content_type="application/json")

def send_new_bug_email(username, email, project, bugTitle, description, attachments):
    portal = "BUGS@YOGASMOGA"

    data = {}

    data['project'] = project
    data['description'] = description
    data['username'] = username
    data['portal'] = portal
    data['bugTitle'] = bugTitle

    # result = Mail::send('emails.new-bug', data, def(message) use (email, attachments)
    #     message.to(email)
    #     message.subject('New bug added at yogasmoga')
    #     message.from('info@yogasmoga.com')
    # )
