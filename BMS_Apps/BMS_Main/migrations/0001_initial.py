# Generated by Django 3.1.5 on 2022-07-04 04:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BmsAccessControlRFID',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rfid_number', models.PositiveBigIntegerField()),
                ('card_type', models.CharField(choices=[('dynamic', 'Dynamic'), ('static', 'Static'), ('no-assign', 'No-assign')], max_length=15)),
                ('access_area', models.JSONField(blank=True, default=list, null=True)),
                ('status', models.CharField(choices=[('active', 'Active'), ('in-active', 'In-active')], max_length=15)),
            ],
            options={
                'db_table': 'bms_access_control_rfid_master',
            },
        ),
        migrations.CreateModel(
            name='BMSHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('history_type', models.CharField(choices=[('new_user', 'New user'), ('visitor', 'Visitor'), ('access', 'Access')], max_length=15)),
                ('description', models.JSONField(blank=True, default=dict, null=True)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of created')),
            ],
            options={
                'db_table': 'bms_history',
            },
        ),
        migrations.CreateModel(
            name='BMSModule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=254)),
                ('module_slug', models.CharField(max_length=254)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('In-active', 'In-active')], max_length=15)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of created')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Date of modified')),
            ],
            options={
                'db_table': 'bms_module_master',
            },
        ),
        migrations.CreateModel(
            name='BMSPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('permission_name', models.CharField(max_length=254)),
                ('permission_slug', models.CharField(max_length=254)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of created')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Date of modified')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMS_Main.bmsmodule')),
            ],
            options={
                'db_table': 'bms_permissions_master',
            },
        ),
    ]
