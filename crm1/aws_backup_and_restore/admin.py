from django.contrib import admin

# Register your models here.
from .models import ProjectDatabase, Buckets, BackupS3

# @admin.register(ProjectDatabase)
# class ProjectDatabaseAdmin(admin.ModelAdmin):
  
#   def save_model(self, request, obj, form, change):
#     obj.user = request.user
#     super().save_model(request, obj, form, change)


admin.site.register(ProjectDatabase)
admin.site.register(Buckets)
admin.site.register(BackupS3)