# Generated by Django 3.1.1 on 2020-12-12 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0005_auto_20201212_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='phone',
            field=models.CharField(default='', max_length=15),
        ),
    ]