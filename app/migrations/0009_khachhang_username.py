# Generated by Django 4.1 on 2022-10-04 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_nhanvienkinhdoanh_xemkhachhang'),
    ]

    operations = [
        migrations.AddField(
            model_name='khachhang',
            name='username',
            field=models.CharField(default=-1, max_length=100),
            preserve_default=False,
        ),
    ]