# Generated by Django 2.0.5 on 2018-05-15 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstApp', '0002_auto_20180515_1417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student_tab',
            name='s_phone',
            field=models.CharField(max_length=200),
        ),
    ]