# Generated by Django 5.0.3 on 2024-06-29 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('date_start', models.DateField()),
                ('estimate_time', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('id_employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.employee')),
                ('id_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.project')),
            ],
        ),
    ]
