# Generated by Django 4.1 on 2022-10-13 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_rename_datataikhoankhachhangxoa_nhanvienpheduyetkhachhangxoa_username'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuanTriVienPheDuyetKhachHangSua',
            new_name='HangDoiQuanTriVienPheDuyet',
        ),
        migrations.DeleteModel(
            name='NhanVienPheDuyetKhachHangXoa',
        ),
        migrations.DeleteModel(
            name='QuanTriVienPheDuyetKhachHangThem',
        ),
    ]