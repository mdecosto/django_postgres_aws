# Generated by Django 4.1.5 on 2023-01-24 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws_backup_and_restore', '0005_remove_projectdatabase_unique_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectdatabase',
            name='unique_id',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
