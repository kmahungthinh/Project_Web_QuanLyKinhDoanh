# Generated by Django 4.1 on 2022-10-13 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_khachhang_covaitro'),
    ]

    operations = [
        migrations.AddField(
            model_name='nguoithamgiakhaosat',
            name='covaitro',
            field=models.BooleanField(default=False),
        ),
    ]