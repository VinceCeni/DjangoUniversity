# Generated by Django 3.1.7 on 2021-03-11 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='djangoClasses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(blank=True, default='', max_length=60)),
                ('instructorName', models.CharField(blank=True, default='', max_length=60)),
                ('courseNumber', models.FloatField(default=0)),
            ],
        ),
    ]
