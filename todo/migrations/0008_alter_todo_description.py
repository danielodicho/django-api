# Generated by Django 3.2.5 on 2021-08-03 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0007_alter_todo_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
