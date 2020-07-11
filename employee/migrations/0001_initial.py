# Generated by Django 3.0.4 on 2020-07-04 04:28

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='Last Name')),
                ('cell_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='Cell no')),
                ('email', models.CharField(blank=True, max_length=50, null=True, verbose_name='Email')),
                ('address', models.TextField(blank=True, null=True, verbose_name='Address')),
                ('employee_no', models.CharField(blank=True, max_length=20, null=True, verbose_name='Employee no')),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, default=None, editable=False, populate_from='first_name', unique=True)),
            ],
        ),
    ]
