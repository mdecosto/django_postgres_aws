# Generated by Django 4.1.5 on 2023-01-24 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aws_backup_and_restore', '0009_projectdatabase_unique_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectdatabase',
            name='unique_id',
            field=models.CharField(default='GFG is best', editable=False, max_length=200),
        ),
    ]
