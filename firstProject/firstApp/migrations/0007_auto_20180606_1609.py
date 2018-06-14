# Generated by Django 2.0.5 on 2018-06-06 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0006_auth_ext'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auth_ext',
            name='user',
            field=models.ForeignKey(blank=True, db_column='user_id', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addittive', to=settings.AUTH_USER_MODEL, to_field='username'),
        ),
    ]