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

    url(r'^is-valid-user', authentication.is_valid_user, name='is_valid_user'),

    url(r'^user-section', user.user_section, name='user_section'),
    url(r'^create-user', user.create_user, name='create_user'),
    url(r'^save-user', user.save_user, name='save_user'),
    url(r'^edit-user/(?P<user_id>\d+)', user.edit_user, name='edit_user'),
    url(r'^remove-user/(?P<user_id>\d+)', user.remove_user, name='remove_user'),
    url(r'^update-user', user.update_user, name='update_user'),
    url(r'^list-users', user.list_users, name='list_users'),
    url(r'^profile', user.profile, name='profile'),
    url(r'^update-profile', user.update_profile, name='update_profile'),

    url(r'^create-project', project.create_project, name='create_project'),
    url(r'^save-project', project.save_project, name='save_project'),
    url(r'^edit-project/(?P<project_id>\d+)', project.edit_project, name='edit_project'),
    url(r'^update-project', project.update_project, name='update_project'),
    url(r'^remove-project/(?P<project_id>\d+)', project.remove_project, name='remove_project'),
    url(r'^list-projects', project.list_projects, name='list_projects'),

    url(r'^create-bug', bug.create_bug, name='create_bug'),
    url(r'^save-bug', bug.save_bug, name='save_bug'),
    url(r'^edit-bug/(?P<bug_id>\d+)', bug.edit_bug, name='edit_bug'),
    url(r'^update-bug', bug.update_bug, name='update_bug'),
    url(r'^list-bugs/(?P<bug_id>\d+)', bug.list_bugs, name='list_bugs'),
    url(r'^save-bug-comment', bug.save_bug_comment, name='save_bug_comment'),
    url(r'^bug-detail/(?P<bug_id>\d+)', bug.bug_detail, name='bug_detail'),
    url(r'^download-bug', bug.download_bug, name='download_bug'),
    url(r'^change-bug-status', bug.change_bug_status, name='change_bug_status'),

    url(r'^data-list-projects', project.data_list_projects, name='data_list_projects'),
    url(r'^data-list-bugs', bug.data_list_bugs, name='data_list_bugs'),
    url(r'^data-list-bug-comments', bug.data_list_bug_comments, name='data_list_bug_comments'),
    url(r'^data-list-users', user.data_list_users, name='data_list_users'),

    url(r'^logout', authentication.logout, name='logout'),

    url(r'^', home.index, name='home'),     # home/index urls should be placed at bottom as it have no url name
]

