# Generated by Django 4.1.7 on 2023-06-15 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0009_alter_profile_online'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rate',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]