from django.db import models

class HangDoiQuanTriVienPheDuyet(models.Model):
    username_old=models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    makhachhang = models.CharField(max_length=100)
    hoten = models.CharField(max_length=100)
    diachi = models.CharField(max_length=100)
    sodienthoai = models.CharField(max_length=12)
    madinhdanh = models.CharField(max_length=100)
    motanoidungyeucau = models.CharField(max_length=100)
    giatien = models.CharField(max_length=100)
    soluongkhaosat = models.IntegerField(default=0)
    socaukhaosat = models.IntegerField(default=0)
    kichhoat = models.BooleanField(default=False)
    hanhdongpheduyet=models.CharField(max_length=100)
class NhanVienPheDuyetBaiKhaoSat(models.Model):
    username_khachhang=models.CharField(max_length=100)
    khaosatso=models.CharField(max_length=100)
    nhanvienquanly=models.CharField(max_length=100)

class NhanVienKinhDoanh(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    manhanvien=models.CharField(max_length=100)
    sodienthoai=models.CharField(max_length=100)
    xemkhachhang = models.BooleanField(default=False)
    themkhachhang=models.BooleanField(default=False)
    xoakhachhang = models.BooleanField(default=False)
    suakhachhang = models.BooleanField(default=False)
    forget_password_token = models.CharField(max_length=100)
    covaitro = models.BooleanField(default=False)
    def __str__(self):
        return self.username
class KhachHang(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    makhachhang = models.CharField(max_length=100)
    hoten = models.CharField(max_length=100)
    diachi = models.CharField(max_length=100)
    sodienthoai = models.CharField(max_length=12)
    madinhdanh = models.CharField(max_length=100)
    motanoidungyeucau = models.CharField(max_length=100)
    giatien = models.IntegerField(default=0)
    soluongkhaosat = models.IntegerField(default=0)
    socaukhaosat = models.IntegerField(default=0)
    kichhoat = models.BooleanField(default=False)
    taocuockhaosat = models.BooleanField(default=False)
    nhanvienquanly=models.CharField(max_length=100)
    forget_password_token= models.CharField(max_length=100)
    covaitro=models.BooleanField(default=False)


    def __str__(self):
        return self.username
class NguoiThamGiaKhaoSat(models.Model):
    username=models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    thongtinkhac = models.CharField(max_length=100)
    sodienthoai=models.CharField(max_length=100)
    thamgiakhaosat = models.CharField(max_length=100)
    khaosat_token = models.CharField(max_length=100)
    ketquakhaosat=models.TextField(default='')
    tien=models.IntegerField(default=0)
    covaitro=models.BooleanField(default=False)
    forget_password_token = models.CharField(max_length=100)

    def __str__(self):
        return self.username
class QuanTriVien(models.Model):
    username=models.CharField(max_length=100)
    covaitro = models.BooleanField(default=False)

    def __str__(self):
        return self.username
class VaiTroTaiKhoan(models.Model):
    username=models.CharField(max_length=100)
    laquantrivien= models.BooleanField(default=False)
    lanhanvienkinhdoanh= models.BooleanField(default=False)
    lakhachhang= models.BooleanField(default=False)
    languoithamgiakhaosat= models.BooleanField(default=False)
    def __str__(self):
        return self.username
class BaiKhaoSat(models.Model):
    username_khachhang=models.CharField(max_length=100)
    khaosatso=models.IntegerField(default=0)
    dulieukhaosat=models.TextField(default='')
    pheduyet = models.BooleanField(default=False)
    def __str__(self):
        return self.username



