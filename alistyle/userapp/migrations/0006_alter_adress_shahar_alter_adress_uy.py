# Generated by Django 4.0.2 on 2022-03-05 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_alter_adress_zipcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='shahar',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='adress',
            name='uy',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]