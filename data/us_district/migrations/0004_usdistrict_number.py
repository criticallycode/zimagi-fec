# Generated by Django 3.0 on 2020-10-04 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('us_district', '0003_auto_20201004_1343'),
    ]

    operations = [
        migrations.AddField(
            model_name='usdistrict',
            name='number',
            field=models.IntegerField(null=True),
        ),
    ]