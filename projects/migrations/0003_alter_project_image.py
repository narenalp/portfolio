# Generated by Django 5.0.6 on 2024-06-30 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_project_image_alter_project_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.CharField(max_length=100),
        ),
    ]
