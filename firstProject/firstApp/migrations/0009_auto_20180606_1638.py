# Generated by Django 2.0.5 on 2018-06-06 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0008_authuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auth_user_extended',
            name='user',
        ),
        migrations.DeleteModel(
            name='auth_user_extended',
        ),
    ]
