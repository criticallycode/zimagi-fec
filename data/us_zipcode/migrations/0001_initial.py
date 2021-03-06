# Generated by Django 3.0 on 2020-10-04 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('us_state', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='USZipcode',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('name', models.CharField(editable=False, max_length=256)),
                ('state', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='uszipcode_relation', to='us_state.USState')),
            ],
            options={
                'verbose_name': 'us zipcode',
                'verbose_name_plural': 'us zipcodes',
                'db_table': 'fec_us_zipcode',
                'ordering': ['name'],
                'abstract': False,
                'unique_together': {('state', 'name')},
            },
        ),
    ]
