from django.db import models

# Create your models here.

class ProjectDatabase(models.Model):
    name = models.CharField(max_length=200, null=True)
    host_url = models.CharField(max_length=300)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    port = models.CharField(max_length=200)
    database_name = models.CharField(max_length=200)
    unique_id = models.CharField(max_length=200, editable=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
  
  
class Buckets(models.Model):
    project = models.ForeignKey(ProjectDatabase, null=True, on_delete = models.PROTECT)
    bucket_name = models.CharField(max_length=300)
    aws_access_key_id = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
  
  
class BackupS3(models.Model):
    project = models.ForeignKey(ProjectDatabase, null=True, on_delete = models.PROTECT)
    file_name = models.CharField(max_length=300)
    bucket_name = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)