# Generated by Django 4.1 on 2022-10-13 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_rename_quantrivienpheduyetkhachhangsua_hangdoiquantrivienpheduyet_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hangdoiquantrivienpheduyet',
            name='hanhdongpheduyet',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
