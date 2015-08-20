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
    url(r'^bugsdjango/', home.index, name='home'),

    url(r'^bugsdjango/is-valid-user', authentication.is_valid_user, name='is-valid-user'),

    url(r'^bugsdjango/user-section', user.user_section, name='user-section'),
    url(r'^bugsdjango/create-user', user.create_user, name='create-user'),
    url(r'^bugsdjango/save-user', user.save_user, name='save-user'),
    url(r'^bugsdjango/edit-user/(?P<user_id>\d+)', user.edit_user, name='edit-user'),
    url(r'^bugsdjango/remove-user/(?P<user_id>\d+)', user.remove_user, name='remove-user'),
    url(r'^bugsdjango/update-user', user.update_user, name='update-user'),
    url(r'^bugsdjango/list-users', user.list_users, name='list-users'),
    url(r'^bugsdjango/profile', user.profile, name='profile'),
    url(r'^bugsdjango/update-profile', user.update_profile, name='update-profile'),

    url(r'^bugsdjango/create-project', project.create_project, name='create-project'),
    url(r'^bugsdjango/save-project', project.save_project, name='save-project'),
    url(r'^bugsdjango/edit-project/(?P<project_id>\d+)', project.edit_project, name='edit-project'),
    url(r'^bugsdjango/update-project', project.update_project, name='update-project'),
    url(r'^bugsdjango/remove-project/(?P<project_id>\d+)', project.remove_project, name='remove-project'),
    url(r'^bugsdjango/list-projects', project.list_projects, name='list-projects'),

    url(r'^bugsdjango/create-bug', bug.create_bug, name='create-bug'),
    url(r'^bugsdjango/save-bug', bug.save_bug, name='save-bug'),
    url(r'^bugsdjango/edit-bug/(?P<bug_id>\d+)', bug.edit_bug, name='edit-bug'),
    url(r'^bugsdjango/update-bug', bug.update_bug, name='updateBug'),
    url(r'^bugsdjango/list-bugs/(?P<bug_id>\d+)', bug.list_bugs, name='list-bugs'),
    url(r'^bugsdjango/save-bug-comment', bug.save_bug_comment, name='save-bug-comment'),
    url(r'^bugsdjango/bug-detail/(?P<bug_id>\d+)', bug.bug_detail, name='bug-detail'),
    url(r'^bugsdjango/download-bug', bug.download_bug, name='download-bug'),
    url(r'^bugsdjango/change-bug-status', bug.change_bug_status, name='change-bug-status'),

    url(r'^bugsdjango/data-list-projects', project.data_list_projects, name='data-list-projects'),
    url(r'^bugsdjango/data-list-bugs', bug.data_list_bugs, name='data-list-bugs'),
    url(r'^bugsdjango/data-list-bug-comments', bug.data_list_bug_comments, name='data-list-bug-comments'),
    url(r'^bugsdjango/data-list-users', user.data_list_users, name='data-list-users'),

    url(r'^bugsdjango/logout', authentication.logout, name='logout')

]

