from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import backup_database, restore_database, ProjectDatabaseViewset, BucketsViewset, BackupS3Viewset


urlpatterns = [
    path('backup-db', backup_database, name='backup_db'),
    path('restore-db', restore_database, name='restore_db'),
]

routers = DefaultRouter()
routers.register(r'project-database', ProjectDatabaseViewset, basename='project-database')
routers.register(r'buckets', BucketsViewset, basename='buckets')
routers.register(r'backup-s3', BackupS3Viewset, basename='backup-s3')


urlpatterns += routers.urls