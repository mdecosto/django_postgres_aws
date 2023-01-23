from django.shortcuts import render
from django.http import HttpResponse
from .tasks import backup_aws_func, restore_from_backup



def backup_database(request):
    backup_aws_func.delay()
    return HttpResponse("Done")
  
def restore_database(request):
    restore_from_backup.delay()
    return HttpResponse("Done")

# Create your views here.
