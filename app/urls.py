"""bugsdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bugsdjango/', home.home, name='home'),

    url(r'^bugsdjango/is-valid-user', authentication.is_valid_user, name='isValidUser'),

    url(r'^bugsdjango/user-section', user.user_section, name='userSection'),
    url(r'^bugsdjango/create-user', user.create_user, name='createUser'),
    url(r'^bugsdjango/save-user', user.save_user, name='saveUser'),
    url(r'^bugsdjango/edit-user/(?P<user_id>\d+)', user.edit_user, name='editUser'),
    url(r'^bugsdjango/remove-user/(?P<user_id>\d+)', user.remove_user, name='removeUser'),
    url(r'^bugsdjango/update-user', user.update_user, name='updateUser'),
    url(r'^bugsdjango/list-users', user.list_users, name='listUsers'),
    url(r'^bugsdjango/profile', user.profile, name='profile'),
    url(r'^bugsdjango/update-profile', user.update_profile, name='updateProfile'),

    url(r'^bugsdjango/create-project', project.create_project, name='createProject'),
    url(r'^bugsdjango/save-project', project.save_project, name='saveProject'),
    url(r'^bugsdjango/edit-project/(?P<project_id>\d+)', project.edit_project, name='editProject'),
    url(r'^bugsdjango/update-project', project.update_project, name='updateProject'),
    url(r'^bugsdjango/remove-project/(?P<project_id>\d+)', project.remove_project, name='removeProject'),
    url(r'^bugsdjango/list-projects', project.list_projects, name='listProjects'),

    url(r'^bugsdjango/create-bug', bug.create_bug, name='createBug'),
    url(r'^bugsdjango/save-bug', bug.save_bug, name='saveBug'),
    url(r'^bugsdjango/edit-bug/(?P<bug_id>\d+)', bug.edit_bug, name='editBug'),
    url(r'^bugsdjango/update-bug', bug.update_bug, name='updateBug'),
    url(r'^bugsdjango/list-bugs/(?P<bug_id>\d+)', bug.list_bugs, name='listBugs'),
    url(r'^bugsdjango/save-bug-comment', bug.save_bug_comment, name='saveBugComment'),
    url(r'^bugsdjango/bug-detail/(?P<bug_id>\d+)', bug.bug_detail, name='bugDetail'),
    url(r'^bugsdjango/download-bug', bug.download_bug, name='downloadBug'),
    url(r'^bugsdjango/change-bug-status', bug.change_bug_status, name='changeBugStatus'),

    url(r'^bugsdjango/data-list-projects', project.data_list_projects, name='dataListProjects'),
    url(r'^bugsdjango/data-list-bugs', bug.data_list_bugs, name='dataListBugs'),
    url(r'^bugsdjango/data-list-bug-comments', bug.data_list_bug_comments, name='dataListBugComments'),
    url(r'^bugsdjango/data-list-users', user.data_list_users, name='dataListUsers'),

    url(r'^bugsdjango/logout', authentication.logout, name='logout')

]

