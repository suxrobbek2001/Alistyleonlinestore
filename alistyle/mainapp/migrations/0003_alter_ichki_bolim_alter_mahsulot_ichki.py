# Generated by Django 4.0.2 on 2022-02-25 11:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_mahsulot_ichki'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ichki',
            name='bolim',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ichki_bolimlar', to='mainapp.bolim'),
        ),
        migrations.AlterField(
            model_name='mahsulot',
            name='ichki',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ichki'),
        ),
    ]