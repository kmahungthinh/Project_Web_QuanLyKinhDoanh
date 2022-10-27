# Generated by Django 4.1 on 2022-10-04 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KhachHang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('makhachhang', models.CharField(max_length=100)),
                ('hoten', models.CharField(max_length=100)),
                ('diachi', models.CharField(max_length=100)),
                ('sodienthoai', models.CharField(max_length=12)),
                ('madinhdanh', models.CharField(max_length=100)),
                ('motanoidungyeucau', models.CharField(max_length=100)),
                ('giatien', models.CharField(max_length=100)),
                ('soluongkhaosat', models.IntegerField(default=0)),
                ('socaukhaosat', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='NguoiThamGiaKhaoSat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thongtinkhac', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='NhanVienKinhDoanh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sodienthoai', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='order',
            name='product',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]