# Generated by Django 4.1 on 2022-10-04 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_nhanvienkinhdoanh_suakhachhang_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhanvienkinhdoanh',
            name='xemkhachhang',
            field=models.BooleanField(default=False),
        ),
    ]
