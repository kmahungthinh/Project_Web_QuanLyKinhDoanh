# Generated by Django 4.1 on 2022-10-09 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_nguoithamgiakhaosat_tien'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminpheduyetkhachhangsua',
            name='giatien',
            field=models.IntegerField(default=0),
        ),
    ]