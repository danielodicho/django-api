# Generated by Django 3.2.5 on 2021-08-05 05:47

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0024_auto_20210804_2009'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='todo_list',
        ),
        migrations.AddField(
            model_name='student',
            name='todo_doing',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='student',
            name='todo_done',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='student',
            name='todo_todo',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='student',
            name='todo_backlog',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=1000), blank=True, null=True, size=None),
        ),
    ]