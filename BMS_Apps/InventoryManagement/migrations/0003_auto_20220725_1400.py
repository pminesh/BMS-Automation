# Generated by Django 3.1.5 on 2022-07-25 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InventoryManagement', '0002_auto_20220725_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetail',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
