from django.urls import path
from . import views


urlpatterns = [
    path('backup_db', views.backup_database, name='backup_db'),
    path('restore_db', views.restore_database, name='restore_db'),
]
