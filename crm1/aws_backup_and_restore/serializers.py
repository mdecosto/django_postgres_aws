from rest_framework import serializers
from .models import ProjectDatabase, Buckets, BackupS3


class ProjectDatabaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDatabase
        fields = '__all__'
    
    
class BucketsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buckets
        fields = '__all__'
    
    
class BackupS3Serializer(serializers.ModelSerializer):
    class Meta:
        model = BackupS3
        fields = '__all__'