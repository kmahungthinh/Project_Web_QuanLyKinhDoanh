# Generated by Django 4.1 on 2022-10-07 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0024_remove_adminpheduyetkhachhangthem_forget_password_token_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='password',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]