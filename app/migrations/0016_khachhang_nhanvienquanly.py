# Generated by Django 4.1 on 2022-10-07 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_remove_khachhang_thamgiakhaosat_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='khachhang',
            name='nhanvienquanly',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
