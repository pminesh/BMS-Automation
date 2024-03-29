# Generated by Django 3.1.5 on 2022-07-05 11:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Areas', '0003_auto_20220705_1710'),
        ('BMS_Main', '0002_auto_20220704_0949'),
    ]

    operations = [
        migrations.AddField(
            model_name='bmsaccesscontrolrfid',
            name='access_end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bmsaccesscontrolrfid',
            name='access_start_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bmshistory',
            name='history_type',
            field=models.CharField(choices=[('new_user', 'New user'), ('visitor', 'Visitor'), ('access', 'Access'), ('conference', 'Conference')], max_length=15),
        ),
        migrations.CreateModel(
            name='BMSSettings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('setting_data', models.JSONField(blank=True, default=dict, null=True)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of created')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BMS_Main.bmsmodule')),
            ],
            options={
                'db_table': 'bms_settings',
            },
        ),
        migrations.CreateModel(
            name='BMSLocker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('normal', 'Normal'), ('big', 'Big')], max_length=15)),
                ('locker_name', models.CharField(max_length=254)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of created')),
                ('subArea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Areas.subarea')),
            ],
            options={
                'db_table': 'bms_locker',
            },
        ),
    ]
