# Generated by Django 3.0 on 2020-10-04 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('candidacy', '0004_auto_20201004_1343'),
        ('year', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidacy',
            name='year',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='candidacy_relation', to='year.Year'),
        ),
    ]
