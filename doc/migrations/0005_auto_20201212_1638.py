# Generated by Django 3.1.1 on 2020-12-12 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doc', '0004_auto_20201212_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientdetails',
            name='phone',
            field=models.IntegerField(default='', max_length=15),
        ),
    ]
