# Generated by Django 4.1 on 2022-10-08 01:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0025_adminpheduyetkhachhangthem_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminpheduyetkhachhangsua',
            old_name='datataikhoankhachhangsua',
            new_name='diachi',
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='diachinew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='emailnew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='giatien',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='giatiennew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='hoten',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='hotennew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='kichhoat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='kichhoatnew',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='madinhdanh',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='madinhdanhnew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='makhachhang',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='makhachhangnew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='motanoidungyeucau',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='motanoidungyeucaunew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='password',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='passwordnew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='socaukhaosat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='socaukhaosatnew',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='sodienthoai',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='sodienthoainew',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='soluongkhaosat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='soluongkhaosatnew',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangsua',
            name='usernamenew',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
