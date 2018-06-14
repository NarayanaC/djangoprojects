# Generated by Django 2.0.5 on 2018-06-05 07:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('firstApp', '0005_auto_20180604_1217'),
    ]

    operations = [
        migrations.CreateModel(
            name='auth_ext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=50)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='addittive', to=settings.AUTH_USER_MODEL, to_field='username')),
            ],
        ),
    ]
