from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', viewIndex, name= 'index'),
    path('dangnhap', viewDangNhap),
    path('dangky', viewDangKy),
    path('quenmatkhau', viewQuenMatKhau),
    path('doimatkhau', viewDoiMatKhau),
    path('datlaimatkhau/<token>' , viewDatLaiMatKhau ),
    path('dangxuat/',auth_views.LogoutView.as_view(next_page='/')),

    path('nhanvien', viewNhanVien),
    path('quanlykhachhang/themmoitaikhoan', viewThemMoiTaiKhoanKhachHang),
    path('quanlykhachhang/themvaodanhsach', viewThemKhachHangVaoDanhSach),
    #path('capnhatkhachhang/<int:id>', viewCapNhatSuaKhachHangVaoQuanTriVienPheDuyet),
    path('quanlykhachhang/<int:id>/xoataikhoankhachhang', viewXoaTaiKhoanKhachHang),
    path('quanlykhachhang/<int:id>/xoakhachhangkhoidanhsach', viewXoaKhachHangKhoiDanhSach),
    path('quanlykhachhang/<int:id>/sua', viewSuaTaiKhoanKhachHang),
    path('quanlykhachhang/hienthi', viewhienThiDanhSachKhachHang),

    path('khachhang', viewKhachHang),
    path('khachhang/taocuockhaosat', viewTaoCuocKhaoSat),
    path('khaosat/hienthidanhsach', viewHienThiDanhSachKhaoSat),
    path('khaosat/<int:id1>/quanlynguoithamgia/<int:id2>/xoataikhoan', viewXoaTaiKhoanNguoiThamGiaKhaoSat),
    path('khaosat/<int:id1>/quanlynguoithamgia/<int:id2>/capnhat', viewCapNhatTaiKhoanNguoiThamGiaKhaoSat),
    path('khaosat/<int:id>/quanlynguoithamgia/hienthi', viewHienThiNguoiThamGiaKhaoSat),
    path('khaosat/<int:id>/quanlynguoithamgia/themtaikhoan', viewThemTaiKhoanNguoiThamGiaKhaoSat),
    path('khaosat/<int:id>/quanlynguoithamgia/themvaocuockhaosat', viewThemNguoiVaoCuocKhaoSat),
    path('khaosat/<int:id1>/quanlynguoithamgia/<int:id2>/sua', viewSuaTaiKhoanNguoiThamGiaKhaoSat),
    path('khaosat/<int:id1>/quanlynguoithamgia/<int:id2>/xoakhoicuockhaosat', viewXoaNguoiThamGiaKhaoSatKhoiKhaoSat),
    path('khaosat/<int:id1>/quanlybaikhaosat/hienthi', viewHienThiBaiKhaoSat),
    path('khaosat/<int:id1>/baichonguoithamgia/<int:id2>/<int:tien>/<token>', viewBaiKhaoSatChoNguoiThamGia),
    path('khaosat/<int:id1>/quanlynguoithamgia/<int:id2>/xemketqua', viewKhachHangXemKetQuaBaiKhaoSat),

    path('quantrivien', viewQuanTriVien),
    path('quantrivien/pheduyet/quanlytaikhoankhachhang/them',viewQuanTriVienPheDuyetThemTaiKhoanKhachHang),
    path('quantrivien/pheduyet/quanlytaikhoankhachhang/them/<int:id>',viewPheDuyetThemTaiKhoanKhachHang),
    path('quantrivien/pheduyet/quanlytaikhoankhachhang/sua', viewQuanTriVienPheDuyetSuaTaiKhoanKhachHang),
    path('quantrivien/pheduyet/quanlytaikhoankhachhang/xoa',viewQuanTriVienPheDuyetXoaTaiKhoanKhachHang),
    path('quantrivien/pheduyet/quanlytaikhoankhachhang/xoa/<int:id>',viewPheDuyetXoaTaiKhoanKhachHang),
    path('quantrivien/pheduyet/quanlytaikhoankhachhang/sua/<int:id>', viewPheDuyetSuaTaiKhoanKhachHang),
    path('quantrivien/pheduyet/quanlytaikhoankhachhang/sua/<int:id>/thongtincu', viewPheDuyetSuaXemThongTinCu),
    path('khaosat/<int:id>/baikhaosat/hienthi',viewHienThiBaiKhaoSat),
    path('khaosat/<int:id1>/baikhaosat/sua/<int:id2>',viewSuaBaiKhaoSat),


    path('nhanvien/pheduyet/hangdoikhaosat',viewNhanVienPheDuyetBaiKhaoSat),
    path('nhanvien/pheduyet/hangdoikhaosat/<int:id>/hienthi',viewNhanVienXemBaiKhaoSat),
    path('nhanvien/pheduyet/hangdoikhaosat/<int:id>/sua',viewNhanVienPheDuyetKhaoSat),

    path('nguoithamgiakhaosat', viewNguoiThamGiaKhaoSat),
    path('nguoithamgiakhaosat/xemsodu', viewNguoiThamGiaKhaoSatXemSoDu),

    path('quantrivien/quanlyvaitro',viewQuanTriVienQuanLyVaiTro),
    path('quantrivien/quanlyphanquyen/nhanvienkinhdoanh',viewQuanTriVienQuanLyPhanQuyen)
]