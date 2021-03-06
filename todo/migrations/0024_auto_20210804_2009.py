# Generated by Django 3.2.5 on 2021-08-05 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0023_alter_download_link_checkpoint'),
    ]

    operations = [
        migrations.CreateModel(
            name='School_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='class_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='todo.school_class'),
        ),
    ]
