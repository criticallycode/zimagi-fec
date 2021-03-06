# Generated by Django 3.0 on 2020-09-27 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('environment', '0002_auto_20190520_0649'),
    ]

    operations = [
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('created', models.DateTimeField(editable=False, null=True)),
                ('updated', models.DateTimeField(editable=False, null=True)),
                ('id', models.CharField(editable=False, max_length=64, primary_key=True, serialize=False)),
                ('transaction_id', models.CharField(max_length=256, null=True)),
                ('year', models.IntegerField(null=True)),
                ('type', models.CharField(max_length=10, null=True)),
                ('amount', models.FloatField(null=True)),
                ('first_name', models.CharField(max_length=256, null=True)),
                ('middle_name', models.CharField(max_length=256, null=True)),
                ('last_name', models.CharField(max_length=256, null=True)),
                ('address_1', models.CharField(max_length=256, null=True)),
                ('address_2', models.CharField(max_length=256, null=True)),
                ('city', models.CharField(max_length=256, null=True)),
                ('state', models.CharField(max_length=256, null=True)),
                ('zip', models.IntegerField(null=True)),
                ('employer', models.CharField(max_length=256, null=True)),
                ('occupation', models.CharField(max_length=256, null=True)),
                ('environment', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='receipt_relation', to='environment.Environment')),
            ],
            options={
                'verbose_name': 'receipt',
                'verbose_name_plural': 'receipts',
                'db_table': 'fec_receipt',
                'ordering': ['first_name', 'middle_name', 'last_name'],
                'abstract': False,
                'unique_together': {('environment', 'transaction_id')},
            },
        ),
    ]
