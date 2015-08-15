from django.db import models

# Create your models here.
class Bug(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    severity = models.CharField(max_length=255)
    created_by = models.IntegerField
    project_id = models.IntegerField
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField('created_at')

class BugComment(models.Model):
    comment = models.CharField(max_length=1000)
    created_by = models.IntegerField
    bug_id = models.IntegerField
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField('created_at')

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    user_type = models.CharField(max_length=255)
    profile_image_name = models.CharField(max_length=255)
    profile_image_saved_name = models.CharField(max_length=255)
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField('created_at')

class BugFile(models.Model):
    file_name = models.CharField(max_length=255)
    saved_file_name = models.CharField(max_length=255)
    bug_id = models.IntegerField
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField('created_at')

class BugCommentFile(models.Model):
    file_name = models.CharField(max_length=255)
    saved_file_name = models.CharField(max_length=255)
    bug_comment_id = models.IntegerField
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField('created_at')

class BugUser(models.Model):
    bug_id = models.IntegerField
    user_id = models.IntegerField
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField('created_at')

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    created_by = models.IntegerField
    status = models.CharField(max_length=50)
    created_at = models.DateTimeField('created_at')