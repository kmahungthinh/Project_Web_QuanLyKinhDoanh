# Generated by Django 4.1 on 2022-10-07 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_quantrivien'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminPheDuyetKhachHangSua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datataikhoankhachhangsua', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='AdminPheDuyetKhachHangXoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datataikhoankhachhangxoa', models.CharField(max_length=100)),
            ],
        ),
        migrations.RenameField(
            model_name='adminpheduyetkhachhangthem',
            old_name='datataikhoankhachhangthem',
            new_name='diachi',
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='email',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='forget_password_token',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='giatien',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='hoten',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='kichhoat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='madinhdanh',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='makhachhang',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='motanoidungyeucau',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='nhanvienquanly',
            field=models.CharField(default=11, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='socaukhaosat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='sodienthoai',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='soluongkhaosat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='adminpheduyetkhachhangthem',
            name='username',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
