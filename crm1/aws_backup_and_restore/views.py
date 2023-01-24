from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from .tasks import backup_aws_func, restore_from_backup
from rest_framework import viewsets
from rest_framework.decorators import api_view
import uuid, psycopg2


from .models import ProjectDatabase, Buckets, BackupS3
from .serializers import ProjectDatabaseSerializer, BucketsSerializer, BackupS3Serializer


def backup_database(request):
    backup_aws_func.delay()
    return HttpResponse("Done backup")
  
def restore_database(request):
    restore_from_backup.delay()
    return HttpResponse("Done restore")

def postgres_test(db_name, user, host, password, port):
    '''test postgres db if working'''
    try:
        conn = psycopg2.connect(f"dbname='{db_name}' user='{user}' host='{host}' password='{password}' port={port}")
        conn.close()
        return True
    except:
        return False


class ProjectDatabaseViewset(viewsets.ModelViewSet):
    queryset = ProjectDatabase.objects.all()
    serializer_class = ProjectDatabaseSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = ProjectDatabase.objects.all()
        serializer = ProjectDatabaseSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        name = request.data.get('name', None)
        host_url = request.data.get('host_url', None)
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        port = request.data.get('port', 5432)
        database_name = request.data.get('database_name', None)
        unique_id = uuid.uuid4()
        date_created = request.data.get('date_created', None)
        
        if postgres_test(db_name=database_name, user=username, host=host_url, password=password, port=port):
            
            new_project_data = ProjectDatabase.objects.create(name=name, host_url=host_url, username=username, password=password, port=port, database_name=database_name, unique_id=unique_id, date_created=date_created)
            
            new_project_data.save()
            serializer = ProjectDatabaseSerializer(new_project_data)
            
            return Response(serializer.data)
        else:
            return Response({"err": "check parameters"})


class BucketsViewset(viewsets.ModelViewSet):
    queryset = Buckets.objects.all()
    serializer_class = BucketsSerializer


class BackupS3Viewset(viewsets.ModelViewSet):
    queryset = BackupS3.objects.all()
    serializer_class = BackupS3Serializer
