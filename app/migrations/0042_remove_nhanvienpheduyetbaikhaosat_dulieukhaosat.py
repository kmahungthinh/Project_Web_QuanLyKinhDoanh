# Generated by Django 4.1 on 2022-10-10 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_rename_adminpheduyetbaikhaosat_nhanvienpheduyetbaikhaosat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nhanvienpheduyetbaikhaosat',
            name='dulieukhaosat',
        ),
    ]