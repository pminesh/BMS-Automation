# Generated by Django 3.1.5 on 2022-07-15 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoodOrdering', '0003_auto_20220705_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodmenu',
            name='image',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='foodorderdetails',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('in-process', 'In-process'), ('completed', 'Completed'), ('cancel', 'Cancel')], default='pending', max_length=15),
        ),
    ]
