# Generated by Django 3.2.5 on 2021-08-05 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0022_auto_20210804_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='download_link',
            name='checkpoint',
            field=models.IntegerField(default=0),
        ),
    ]