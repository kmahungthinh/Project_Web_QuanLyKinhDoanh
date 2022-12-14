# Generated by Django 4.1 on 2022-10-12 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0043_vaitrotaikhoan'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AdminPheDuyetKhachHangXoa',
            new_name='NhanVienPheDuyetKhachHangXoa',
        ),
        migrations.RenameModel(
            old_name='AdminPheDuyetKhachHangSua',
            new_name='QuanTriVienPheDuyetKhachHangSua',
        ),
        migrations.RenameModel(
            old_name='AdminPheDuyetKhachHangThem',
            new_name='QuanTriVienPheDuyetKhachHangThem',
        ),
        migrations.AddField(
            model_name='khachhang',
            name='vaitro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nguoithamgiakhaosat',
            name='vaitro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='nhanvienkinhdoanh',
            name='vaitro',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='quantrivien',
            name='vaitro',
            field=models.BooleanField(default=False),
        ),
    ]
