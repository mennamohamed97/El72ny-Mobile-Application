# Generated by Django 4.1.7 on 2023-05-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='Lat',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Lng',
        ),
        migrations.RemoveField(
            model_name='tracking',
            name='profile',
        ),
        migrations.AddField(
            model_name='tracking',
            name='userId',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracking',
            name='userLat',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tracking',
            name='userLng',
            field=models.CharField(default=0, max_length=20),
            preserve_default=False,
        ),
    ]
