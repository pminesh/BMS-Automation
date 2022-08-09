# Generated by Django 3.1.5 on 2022-07-05 11:40

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BMS_Main', '0003_auto_20220705_1710'),
        ('Areas', '0003_auto_20220705_1710'),
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userstaffdetail',
            name='access_area',
        ),
        migrations.AddField(
            model_name='userstaffdetail',
            name='locker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BMS_Main.bmslocker'),
        ),
        migrations.AddField(
            model_name='uservisitordetail',
            name='locker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BMS_Main.bmslocker'),
        ),
        migrations.AlterField(
            model_name='userstaffdetail',
            name='department',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Areas.department'),
        ),
        migrations.CreateModel(
            name='UserWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wallet_balance', models.DecimalField(decimal_places=2, max_digits=9)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.userbms')),
            ],
            options={
                'db_table': 'bms_user_wallet',
            },
        ),
        migrations.CreateModel(
            name='UserVisitorActivity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meet_person_name', models.CharField(max_length=254)),
                ('in_time', models.TimeField()),
                ('out_time', models.TimeField()),
                ('reason_to_meet', models.TextField()),
                ('out_remark', models.CharField(max_length=254)),
                ('rfid', models.CharField(max_length=254)),
                ('status', models.CharField(choices=[('in', 'In'), ('out', 'Out')], max_length=15)),
                ('access_from_time', models.TimeField()),
                ('access_to_time', models.TimeField()),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of created')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Date of modified')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Areas.department')),
                ('enter_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enter_by', to='Users.userbms')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to='Users.userbms')),
            ],
            options={
                'db_table': 'bms_visitor_activity ',
            },
        ),
        migrations.CreateModel(
            name='UserRechargeWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recharge_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('wallet_balance', models.DecimalField(decimal_places=2, max_digits=9)),
                ('createdAt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date of created')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.userbms')),
            ],
            options={
                'db_table': 'bms_recharge_wallet',
            },
        ),
    ]
