# Generated by Django 4.1 on 2022-10-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_adminpheduyetkhachhangsua_adminpheduyetkhachhangxoa_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminpheduyetkhachhangthem',
            name='forget_password_token',
        ),
        migrations.RemoveField(
            model_name='adminpheduyetkhachhangthem',
            name='nhanvienquanly',
        ),
    ]
