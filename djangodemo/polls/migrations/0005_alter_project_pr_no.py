# Generated by Django 3.2.7 on 2021-09-22 07:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_alter_project_pr_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='pr_no',
            field=models.IntegerField(default=1, unique=True, validators=[django.core.validators.MinValueValidator(30)]),
        ),
    ]
