# Generated by Django 4.1 on 2022-10-07 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_khachhang_nhanvienquanly'),
    ]

    operations = [
        migrations.AddField(
            model_name='nhanvienkinhdoanh',
            name='manhanvien',
            field=models.CharField(default=-1, max_length=100),
            preserve_default=False,
        ),
    ]
