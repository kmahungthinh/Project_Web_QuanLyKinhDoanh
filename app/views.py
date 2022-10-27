from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
import uuid
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .helpers import *
from django.db.models import Q
from flask import Flask
app = Flask(__name__)


# Create your views here.

#======================================FORM USER=======================================================================
def viewIndex(request):
    if request.method == 'POST' and 'dangnhap' in request.POST:
        return redirect('/dangnhap')
    if request.method == 'POST' and 'dangky' in request.POST:
        return redirect('/dangky')
    return render(request, 'index.html')
def viewDangKy(request):
    msg = None
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()

            vaitro=VaiTroTaiKhoan()
            username = request.POST.get('username')
            vaitro.username=username
            vaitro.lakhachhang=1
            vaitro.save()

            kh = KhachHang()
            email = request.POST.get('email')
            kh.username=username
            kh.email=email
            kh.covaitro=1
            kh.save()

            msg = 'Đăng ký thành công'
            return render(request,'taikhoannguoidung/dangky.html', {'form': form, 'msg': msg})
        else:
            print("error")
            return render(request, 'taikhoannguoidung/dangky.html', {'form': form, 'msg': msg})
    return render(request,'taikhoannguoidung/dangky.html', {'form': form, 'msg': msg})
def viewDangNhap(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if User.objects.filter(username=username).exists() == False:
                msg = 'Đăng nhập không hợp lệ'
                return render(request, 'taikhoannguoidung/dangnhap.html', {'form': form, 'msg': msg})
            vaitro=VaiTroTaiKhoan.objects.get(username=username)
            if user is not None and vaitro.lanhanvienkinhdoanh==1:
                login(request, user)
                return redirect('/nhanvien')
            elif user is not None and vaitro.lakhachhang==1:
                kh = KhachHang.objects.get(username=username)
                if kh.kichhoat==0:
                    msg = 'Tài khoản khách hàng này chưa được kích hoạt'
                else:
                    login(request, user)
                    return redirect('/khachhang')
            elif user is not None and vaitro.laquantrivien == 1:
                login(request, user)
                return redirect('/quantrivien')
            elif user is not None and vaitro.languoithamgiakhaosat == 1:
                login(request, user)
                return redirect('/nguoithamgiakhaosat')
            else:
                msg = 'Đăng nhập không hợp lệ'
        else:
            msg = 'Form đăng nhập không hợp lệ'
    return render(request, 'taikhoannguoidung/dangnhap.html', {'form': form, 'msg': msg})
def viewDoiMatKhau(request):
    msg = None
    if str(request.user) == 'AnonymousUser':
        print("thoa man")
        return redirect('/nhanvien')
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            msg = 'Đổi mật khẩu thành công'
            return render(request, 'taikhoannguoidung/doimatkhau.html',{'form': form, 'msg': msg
                , 'nguoidung': str(request.user)})
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'taikhoannguoidung/doimatkhau.html', {'form': form, 'msg': msg, 'nguoidung':str(request.user)})
def viewDatLaiMatKhau(request,token):
    context = {}
    try:
        u=None
        if NhanVienKinhDoanh.objects.filter(forget_password_token=token).exists() == True:
            u = NhanVienKinhDoanh.objects.get(forget_password_token=token)
            user = User.objects.get(username=u.username)
            context = {'user_id': user.id}

        elif NguoiThamGiaKhaoSat.objects.filter(forget_password_token=token).exists() == True:
            u = NguoiThamGiaKhaoSat.objects.get(forget_password_token=token)
            user = User.objects.get(username=u.username)
            context = {'user_id': user.id}
        elif KhachHang.objects.filter(forget_password_token=token).exists() == True:
            u = KhachHang.objects.get(forget_password_token=token)
            user = User.objects.get(username=u.username)
            context = {'user_id': user.id}
        #print("user",user.id)

        if request.method == 'POST':
            matkhaudatlai = request.POST.get('matkhaudatlai')
            nhaplaimatkhaudatlai = request.POST.get('nhaplaimatkhaudatlai')

            if matKhauThoaManDinhDangQuyUoc(matkhaudatlai)==False:
                messages.success(request,
                "Mật khẩu mới không đúng định dạng (phải bao gồm: chữ hoa,chữ thường,số, ký tự đặc biệt")
                return redirect(f'/datlaimatkhau/{token}')
            elif matkhaudatlai != nhaplaimatkhaudatlai:
                messages.success(request, 'Mật khẩu nhập mới nhập lại không khớp.')
                return redirect(f'/datlaimatkhau/{token}')
            if NhanVienKinhDoanh.objects.filter(forget_password_token=token).exists() == True:
                u = NhanVienKinhDoanh.objects.get(forget_password_token=token)
            elif NguoiThamGiaKhaoSat.objects.filter(forget_password_token=token).exists() == True:
                u = NguoiThamGiaKhaoSat.objects.get(forget_password_token=token)
            elif KhachHang.objects.filter(forget_password_token=token).exists() == True:
                u = KhachHang.objects.get(forget_password_token=token)
            user = User.objects.get(username=u.username)
            user.set_password(matkhaudatlai)
            user.save()
            return redirect('/dangnhap')
    except Exception as e:
        print(e)
    return render(request, 'taikhoannguoidung/datlaimatkhau.html', context)
def viewQuenMatKhau(request):
    try:
        if request.method == 'POST':
            username = request.POST.get('username')

            if not User.objects.filter(username=username).first():
                messages.success(request, 'Không tìm thấy tài khoản này')
                return redirect('/quenmatkhau')
            token = str(uuid.uuid4())
            if NhanVienKinhDoanh.objects.filter(username=username).exists() == True:
                u = NhanVienKinhDoanh.objects.get(username=username)
            elif NguoiThamGiaKhaoSat.objects.filter(username=username).exists() == True:
                u = NguoiThamGiaKhaoSat.objects.get(username=username)
            elif KhachHang.objects.filter(username=username).exists() == True:
                u = KhachHang.objects.get(username=username)
            u.forget_password_token = token
            u.save()
            user = User.objects.get(username=username)
            guiMailDatLaiMatKhau(user.email, token)
            msg='Một email đã được gửi tới hộp thư của tài khoản '\
                +user.email+' bạn hãy vào đó để xác thực'
            messages.success(request,msg)
            return redirect('/quenmatkhau')
    except Exception as e:
        print(e)
    return render(request, 'taikhoannguoidung/quenmatkhau.html')

#======================================Vai trò=======================================================================
def viewKhachHang(request):
    return render(request,'vaitro/khachhang.html')
def viewNhanVien(request):
    return render(request,'vaitro/nhanvien.html')
def viewQuanTriVien(request):
    return render(request,'vaitro/quantrivien.html')
#======================================Khách hàng================================================================

def viewThemMoiTaiKhoanKhachHang(request):
    nvkq = NhanVienKinhDoanh.objects.get(username=request.user)
    if nvkq.themkhachhang==1:
        khform=QuanTriVienPheDuyetKhachHangThemForm()
        if request.method == 'POST':
            khform = QuanTriVienPheDuyetKhachHangThemForm(request.POST)
            tendangnhap = request.POST.getlist('username')
            tendangnhap = tendangnhap[0]

            if User.objects.filter(username=tendangnhap).exists()==True:
                msg="Tài khoản đã tồn tại"
                return render(request, 'khachhang/themtaikhoan.html', {'msg': msg,'khform':khform})
            elif HangDoiQuanTriVienPheDuyet.objects.filter(Q(username=tendangnhap),Q(hanhdongpheduyet='them')).exists()==True:
                msg="Tài khoản cần thêm này đã tồn tại trong hàng đợi phê duyệt"
                return render(request, 'khachhang/themtaikhoan.html', {'msg': msg,'khform':khform})
            else:
                adthem = HangDoiQuanTriVienPheDuyet()
                adthem.username = request.POST.getlist('username')[0]
                adthem.password = request.POST.getlist('password')[0]
                if matKhauThoaManDinhDangQuyUoc(adthem.password)==False:
                    msg = "Mật khẩu không thỏa mãn định dạng quy ước"
                    return render(request, 'khachhang/themtaikhoan.html', {'msg': msg,'khform':khform})
                adthem.email = request.POST.getlist('email')[0]
                adthem.makhachhang = request.POST.getlist('makhachhang')[0]
                adthem.hoten = request.POST.getlist('hoten')[0]
                adthem.diachi = request.POST.getlist('diachi')[0]
                adthem.sodienthoai = request.POST.getlist('sodienthoai')[0]
                if sdtThoaManDinhDangQuyUoc(adthem.sodienthoai)==False:
                    msg = "SĐT không thỏa mãn định dạng quy ước"
                    return render(request, 'khachhang/themtaikhoan.html', {'msg': msg,'khform':khform})
                adthem.madinhdanh = request.POST.getlist('madinhdanh')[0]
                adthem.motanoidungyeucau = request.POST.getlist('motanoidungyeucau')[0]
                adthem.giatien = request.POST.getlist('giatien')[0]
                adthem.soluongkhaosat = request.POST.getlist('soluongkhaosat')[0]
                adthem.socaukhaosat = request.POST.getlist('socaukhaosat')[0]
                if len(request.POST.getlist('kichhoat')) == 0:
                    adthem.kichhoat = False
                else:
                    adthem.kichhoat = True
                adthem.hanhdongpheduyet='them'
                adthem.save()
                messages.success(request, "Đã gửi đến quản trị viên yêu cầu sửa khách hàng")
                return redirect("/quanlykhachhang/hienthi")
    else:
        return render(request, "error/permission.html",{'nvkd':request.user})
    return render(request, 'khachhang/themtaikhoan.html',{'khform':khform})

def viewThemKhachHangVaoDanhSach(request):
    manv=NhanVienKinhDoanh.objects.get(username=request.user)
    print(manv.manhanvien)
    chua_kh = KhachHang.objects.exclude(Q(nhanvienquanly__icontains=manv.manhanvien)|Q(covaitro=0))
    list_u=[]
    for i in chua_kh:
        list_u.append(i.username)
    if len(list_u)==0:
        return render(request, 'error/themvaodanhsach.html',{'cuockhaosat':id})
    if request.method == 'POST':
        kh = KhachHang.objects.get(
            username=request.POST.getlist('namekhachhangthemvaodanhsach')[0])
        kh.nhanvienquanly = kh.nhanvienquanly + manv.manhanvien
        kh.save()
        return redirect('/quanlykhachhang/hienthi')

    return render(request, 'khachhang/themvaodanhsach.html',{'khachhang': list_u})
def viewhienThiDanhSachKhachHang(request):
    nvkd = NhanVienKinhDoanh.objects.get(username=request.user)
    if nvkd.xemkhachhang==1:
        khachhang = KhachHang.objects.filter(Q(nhanvienquanly__icontains=nvkd.manhanvien),Q(covaitro=1))
        return render(request,"khachhang/hienthi.html",{'khachhang':khachhang})
    else:
        return render(request, "error/permission.html",{'nvkd':request.user})

def viewSuaTaiKhoanKhachHang(request, id):
    nvkq = NhanVienKinhDoanh.objects.get(username=request.user)
    if nvkq.suakhachhang == 1:
        khachhang = KhachHang.objects.get(id=id)

        if request.method == 'POST':

            count=HangDoiQuanTriVienPheDuyet.objects.filter(username=khachhang.username).count()
            if count==1:
                print("thoa man")
                hdpdthem=HangDoiQuanTriVienPheDuyet.objects.get(Q(username=khachhang.username),Q(hanhdongpheduyet='sua'))
                hdpdthem.delete()
            adsua = HangDoiQuanTriVienPheDuyet()
            adsua.username_old=khachhang.username
            adsua.username = request.POST.getlist('username')[0]
            adsua.password = request.POST.getlist('password')[0]
            if matKhauThoaManDinhDangQuyUoc(adsua.password) == False:
                msg = "Mật khẩu không thỏa mãn định dạng quy ước"
                return render(request, 'khachhang/sua.html', {'msg': msg, 'khachhang':khachhang})
            adsua.email = request.POST.getlist('email')[0]
            adsua.makhachhang = request.POST.getlist('makhachhang')[0]
            adsua.hoten = request.POST.getlist('hoten')[0]
            adsua.diachi = request.POST.getlist('diachi')[0]
            adsua.sodienthoai = request.POST.getlist('sodienthoai')[0]
            if sdtThoaManDinhDangQuyUoc(adsua.sodienthoai) == False:
                msg = "SĐT không thỏa mãn định dạng quy ước"
                return render(request, 'khachhang/sua.html', {'msg': msg, 'khachhang':khachhang})
            adsua.madinhdanh = request.POST.getlist('madinhdanh')[0]
            adsua.motanoidungyeucau = request.POST.getlist('motanoidungyeucau')[0]
            adsua.giatien = request.POST.getlist('giatien')[0]
            adsua.soluongkhaosat = request.POST.getlist('soluongkhaosat')[0]
            adsua.socaukhaosat = request.POST.getlist('socaukhaosat')[0]

            print("Kích hoạt",request.POST.getlist('kichhoat'))
            if len(request.POST.getlist('kichhoat')) == 0:
                adsua.kichhoat = False
            else:
                adsua.kichhoat = True
            adsua.hanhdongpheduyet='sua'
            adsua.save()
            messages.success(request, "Đã gửi đến quản trị viên yêu cầu sửa khách hàng")
            return redirect("/quanlykhachhang/hienthi")
        return render(request,'khachhang/sua.html', {'khachhang':khachhang})
    else:
        return render(request, "error/permission.html", {'khachhang': nvkq})
def viewXoaTaiKhoanKhachHang(request, id):
    nvkq = NhanVienKinhDoanh.objects.get(username=request.user)
    if nvkq.xoakhachhang==1:
        hdqtvpd = HangDoiQuanTriVienPheDuyet()
        kh = KhachHang.objects.get(id=id)
        hdqtvpd.username = kh.username
        if HangDoiQuanTriVienPheDuyet.objects.filter(Q(username=kh.username),Q(hanhdongpheduyet='xoa')).exists() == False:
            hdqtvpd.email=kh.email
            hdqtvpd.makhachhang=kh.makhachhang
            hdqtvpd.hoten=kh.hoten
            hdqtvpd.diachi=kh.diachi
            hdqtvpd.madinhdanh=kh.madinhdanh
            hdqtvpd.motanoidungyeucau=kh.motanoidungyeucau
            hdqtvpd.giatien=kh.giatien
            hdqtvpd.soluongkhaosat=kh.soluongkhaosat
            hdqtvpd.socaukhaosat=kh.socaukhaosat
            hdqtvpd.hanhdongpheduyet='xoa'
            hdqtvpd.save()
        messages.success(request, "Đã gửi đến quản trị viên yêu cầu xóa khách hàng")
        return redirect("/quanlykhachhang/hienthi")
    else:
        return render(request, "error/permission.html", {'khachhang': nvkq})
def viewXoaKhachHangKhoiDanhSach(request, id):
    kh = KhachHang.objects.get(id=id)
    nhanvienquanly = kh.nhanvienquanly

    nvkd = NhanVienKinhDoanh.objects.get(username=request.user)
    manhanvien=nvkd.manhanvien
    kh.nhanvienquanly=nhanvienquanly.replace(manhanvien,"",1)
    kh.save()
    khpdks_all = NhanVienPheDuyetBaiKhaoSat.objects.all()
    list_nvpdbks=[]
    for i in khpdks_all:
        list_nvpdbks.append([i.username_khachhang,i.khaosatso])
    print(list_nvpdbks)
    for i in list_nvpdbks:
        print(i[0])
        if i[0]==kh.username:
            nvpdbks = NhanVienPheDuyetBaiKhaoSat.objects.get(khaosatso=i[1])
            print(nvpdbks.khaosatso)
            nhanvienquanly = nvpdbks.nhanvienquanly
            nvpdbks.nhanvienquanly=nhanvienquanly.replace(manhanvien,"",1)
            nvpdbks.save()
    NhanVienPheDuyetBaiKhaoSat.objects.filter(nhanvienquanly="").delete()
    return redirect("/quanlykhachhang/hienthi")


#======================================Khảo sát================================================================
#--------------------------------------Danh sách--------------------------------------------------------------

def viewHienThiDanhSachKhaoSat(request):
    khachhang = KhachHang.objects.get(username=request.user)
    if khachhang.taocuockhaosat==0:
        return redirect("/khachhang/taocuockhaosat")
    soLuongKhaoSat=khachhang.soluongkhaosat
    soLuongKhaoSat = [i for i in range(0, soLuongKhaoSat)]
    return render(request, "hienthidanhsachkhaosat.html", {'soLuongKhaoSat': soLuongKhaoSat})


#--------------------------------------Tài khoản tham gia-------------------------------------------------------
def viewXoaTaiKhoanNguoiThamGiaKhaoSat(request, id1, id2):
    ntgks = NguoiThamGiaKhaoSat.objects.get(id=id2)
    user = User.objects.get(username=ntgks.username)
    ntgks.delete()
    user.delete()
    return redirect('/khaosat/%d/quanlynguoithamgia/hienthi'%id1)
def viewThemTaiKhoanNguoiThamGiaKhaoSat(request, id):
    ntgksform = NguoiThamGiaKhaoSatForm()
    if request.method == 'POST':
        tendangnhap = request.POST.getlist('username')
        tendangnhap = tendangnhap[0]
        matkhau = request.POST.getlist('password')
        matkhau = matkhau[0]
        email = request.POST.getlist('email')
        email = email[0]
        sodienthoai = request.POST.getlist('sodienthoai')
        sodienthoai = sodienthoai[0]
        ntgksform = NguoiThamGiaKhaoSatForm(request.POST)

        if User.objects.filter(username=tendangnhap).exists() == True:
            msg = "Tài khoản đã tồn tại"
            print("Tồn tại")
            return render(request, 'khaosat/nguoithamgiakhaosat/themtaikhoan.html', {'msg': msg, 'form': ntgksform})
        else:
            if matKhauThoaManDinhDangQuyUoc(matkhau) == False:
                ntgksform = NguoiThamGiaKhaoSatForm()
                msg = "Mật khẩu không thỏa mãn định dạng quy ước"
                return render(request,'khaosat/nguoithamgiakhaosat/themtaikhoan.html', {'form': ntgksform,'msg':msg})
            if emailThoaManDinhDangQuyUoc(email) == False:
                ntgksform = NguoiThamGiaKhaoSatForm()
                msg = "Email không thỏa mãn định dạng quy ước"
                return render(request,'khaosat/nguoithamgiakhaosat/themtaikhoan.html', {'form': ntgksform,'msg':msg})
            if sdtThoaManDinhDangQuyUoc(sodienthoai) == False:
                ntgksform = NguoiThamGiaKhaoSatForm()
                msg = "Số điện thoại không thỏa mãn định dạng quy ước"
                return render(request,'khaosat/nguoithamgiakhaosat/themtaikhoan.html', {'form': ntgksform,'msg':msg})
            CreateAccount(tendangnhap, email, matkhau)
            ntgksform.save()

            ntgks=NguoiThamGiaKhaoSat.objects.get(username=tendangnhap)
            ntgks.covaitro=1
            ntgks.save()

            vaitro = VaiTroTaiKhoan()
            vaitro.username = tendangnhap
            vaitro.languoithamgiakhaosat = 1
            vaitro.save()

            return redirect('/khaosat/%d/quanlynguoithamgia/hienthi' % id)
    return render(request,'khaosat/nguoithamgiakhaosat/themtaikhoan.html', {'form': ntgksform})
def viewSuaTaiKhoanNguoiThamGiaKhaoSat(request, id1, id2):
    khachhang = NguoiThamGiaKhaoSat.objects.filter(id=id2)
    return render(request,'khaosat/nguoithamgiakhaosat/sua.html', {'employee':khachhang, 'idurl':id1})
def viewCapNhatTaiKhoanNguoiThamGiaKhaoSat(request, id1, id2):
    if request.method == 'POST':
        datacapnhat=[]
        username = request.POST.getlist('username');username = username[0];datacapnhat.append(username)
        password1 = request.POST.getlist('password1');password1 = password1[0];datacapnhat.append(password1)
        sodienthoai = request.POST.getlist('sodienthoai') ;sodienthoai = sodienthoai[0];datacapnhat.append(sodienthoai)
        email = request.POST.getlist('email') ; email = email[0];datacapnhat.append(email)
        thongtinkhac = request.POST.getlist('thongtinkhac');thongtinkhac = thongtinkhac[0];datacapnhat.append(thongtinkhac)
        sv_capNhatNguoiThamGiaKhaoSat(id2,datacapnhat)
    return redirect('/khaosat/%d/quanlynguoithamgia/hienthi'%id1)
#--------------------------------------Người tham gia-------------------------------------------------------
def viewHienThiNguoiThamGiaKhaoSat(request, id):
    khks = KhachHang.objects.get(username=request.user)
    makhachhang_id=khks.makhachhang+"$"+str(id)
    print("Mã khách hàng", makhachhang_id)
    tgks = NguoiThamGiaKhaoSat.objects.filter(Q(thamgiakhaosat__icontains=makhachhang_id),Q(covaitro=1))


    return render(request, "khaosat/nguoithamgiakhaosat/hienthi.html",{'tgks':tgks,'idurl':id})

def viewXoaNguoiThamGiaKhaoSatKhoiKhaoSat(request, id1, id2):
    ntgks = NguoiThamGiaKhaoSat.objects.get(id=id2)
    thamGiaKhaoSat=ntgks.thamgiakhaosat

    khachang = KhachHang.objects.get(username=request.user)
    makhachhang=khachang.makhachhang
    makhachhang_id=makhachhang+"$"+str(id1)
    ntgks.thamgiakhaosat=thamGiaKhaoSat.replace(makhachhang_id,"",1)
    ntgks.save()
    baikhaosat = BaiKhaoSat.objects.get(Q(username_khachhang=request.user), Q(khaosatso=id1))
    ketquakhaosat=ntgks.ketquakhaosat[0:len(ntgks.ketquakhaosat)-1]
    if len(ketquakhaosat)!=0:
        s=ketquakhaosat.split("&")
        for i in s:
            a=i.split("^")
            if baikhaosat.id==int(a[0]):
                break
        ntgks.ketquakhaosat=ntgks.ketquakhaosat.replace(i+"&","",1)
        ntgks.save()

    return redirect('/khaosat/%d/quanlynguoithamgia/hienthi'%id1)


def viewThemNguoiVaoCuocKhaoSat(request, id):
    khachang = KhachHang.objects.get(username=request.user)
    makhachhang = khachang.makhachhang
    makhachhang_id = makhachhang + "$" + str(id)
    chua_tgks = NguoiThamGiaKhaoSat.objects.exclude(Q(thamgiakhaosat__icontains=makhachhang_id)|Q(covaitro=0))
    list_u=[]
    for i in chua_tgks:
        list_u.append(i.username)
    if len(list_u)==0:
        return render(request, 'error/themvaocuockhaosat.html',{'cuockhaosat':id})
    if request.method == 'POST':
        count = NhanVienPheDuyetBaiKhaoSat.objects.filter(Q(username_khachhang=request.user), Q(khaosatso=id)).count()
        if count==1:
            msg="Cuộc khảo sát này chưa được phê duyệt"
            return render(request, 'khaosat/nguoithamgiakhaosat/themvaocuockhaosat.html',
                      {'taikhoanthamgiakhaosat': list_u, 'cuockhaosat': id,'msg':msg})
        else:
            #Lấy 1 bản ghi từ DB với điều kiện tài khoản = tài khoản được chọn tham gia khảo sát từ drop down list
            nguoithamgiakhaosat = NguoiThamGiaKhaoSat.objects.get(username=request.POST.getlist('nametaikhoanthamgiakhaosat')[0])
            #Người tham gia khảo sát được lưu vào trường thamgiakhaosat gồm mã khách hàng+id của cuộc khảo sát
            nguoithamgiakhaosat.thamgiakhaosat = nguoithamgiakhaosat.thamgiakhaosat + makhachhang_id
            #Lưu lại thông tin
            nguoithamgiakhaosat.save()
            #Lấy 1 bản ghi từ DB với điều kiện tài khoản = tài khoản khách hàng đang dùng, số thứ tự khảo sát = id
            baikhaosat = BaiKhaoSat.objects.get(Q(username_khachhang=request.user), Q(khaosatso=id))
            #Lấy id của bản ghi của dữ liệu trên
            idbaikhaosat=baikhaosat.id
            #Danh sách câu khảo sát dạng list
            caukhaosat = baikhaosat.dulieukhaosat.split("$")
            cks = []
            for i in range(0, len(caukhaosat)):
                cks.append([i, caukhaosat[i]])
            token = str(uuid.uuid4())
            tgks = NguoiThamGiaKhaoSat.objects.get(username=request.POST.getlist('nametaikhoanthamgiakhaosat')[0])
            user=User.objects.get(username=request.POST.getlist('nametaikhoanthamgiakhaosat')[0])
            tgks.khaosat_token = token
            tgks.save()
            #Gửi mail gồm địa chỉ mail , token, id cuộc khảo sát và id baikhaosat
            guiMailToiNguoiThamGiaKhaoSat(user.email, token,id,idbaikhaosat,khachang.giatien)

            return redirect('/khaosat/%d/quanlynguoithamgia/hienthi' % id)
    return render(request,'khaosat/nguoithamgiakhaosat/themvaocuockhaosat.html', {'taikhoanthamgiakhaosat': list_u,'cuockhaosat':id})

#=========================================Phê duyệt=======================================================================
def viewQuanTriVienPheDuyetThemTaiKhoanKhachHang(request):
    hdqtvpdthem=HangDoiQuanTriVienPheDuyet.objects.filter(hanhdongpheduyet='them')
    return render(request, 'quantrivien/pheduyet/quanlytaikhoankhachhang/them.html',{'hdqtvpdthem':hdqtvpdthem})
def viewPheDuyetThemTaiKhoanKhachHang(request,id):
    print(id)
    khthem = HangDoiQuanTriVienPheDuyet.objects.get(id=id)
    listhem=[khthem.username,khthem.password,khthem.makhachhang,khthem.hoten,khthem.diachi,khthem.sodienthoai,
             khthem.madinhdanh,khthem.email, khthem.motanoidungyeucau,khthem.giatien,khthem.soluongkhaosat,
             khthem.socaukhaosat,khthem.kichhoat]
    sv_themKhachHang(listhem)

    vaitro=VaiTroTaiKhoan()
    vaitro.username=khthem.username
    vaitro.lakhachhang=1
    vaitro.save()

    khthem.delete()
    return redirect("/quantrivien/pheduyet/quanlytaikhoankhachhang/them")

def viewPheDuyetSuaXemThongTinCu(request,id):
    qtvpdkhs= HangDoiQuanTriVienPheDuyet.objects.get(id=id)
    thongtincu= KhachHang.objects.get(username=qtvpdkhs.username_old)
    return render(request, 'quantrivien/pheduyet/quanlytaikhoankhachhang/thongtincu.html', {'thongtincu': thongtincu})
def viewQuanTriVienPheDuyetSuaTaiKhoanKhachHang(request):
    hdqtvpdkhsua=HangDoiQuanTriVienPheDuyet.objects.filter(hanhdongpheduyet='sua')
    return render(request, 'quantrivien/pheduyet/quanlytaikhoankhachhang/sua.html',{'hdqtvpdkhsua':hdqtvpdkhsua})

def viewPheDuyetSuaTaiKhoanKhachHang(request, id):
    adsua = HangDoiQuanTriVienPheDuyet.objects.get(id=id)
    khsua=KhachHang.objects.get(username=adsua.username_old)
    khsua.username=adsua.username
    khsua.password=adsua.password
    khsua.makhachhang=adsua.makhachhang
    khsua.hoten=adsua.hoten
    khsua.diachi=adsua.sodienthoai
    khsua.madinhdanh=adsua.madinhdanh
    khsua.email=adsua.email
    khsua.motanoidungyeucau=adsua.motanoidungyeucau
    khsua.giatien=adsua.giatien
    khsua.soluongkhaosat=adsua.soluongkhaosat
    khsua.socaukhaosat=adsua.socaukhaosat
    khsua.kichhoat=adsua.kichhoat
    khsua.save()

    user = User.objects.get(username=adsua.username_old)
    user.username = adsua.username
    user.set_password(adsua.password)
    user.email=adsua.email
    user.save()

    vttk=VaiTroTaiKhoan.objects.get(username=adsua.username_old)
    vttk.username = adsua.username
    vttk.save()

    adsua.delete()
    return redirect("/quantrivien/pheduyet/quanlytaikhoankhachhang/sua")
def viewQuanTriVienPheDuyetXoaTaiKhoanKhachHang(request):
    hdqtvpdkhxoa=HangDoiQuanTriVienPheDuyet.objects.filter(hanhdongpheduyet='xoa')
    return render(request, 'quantrivien/pheduyet/quanlytaikhoankhachhang/xoa.html',{'hdqtvpdkhxoa':hdqtvpdkhxoa})
def viewPheDuyetXoaTaiKhoanKhachHang(request, id):
    adxoa = HangDoiQuanTriVienPheDuyet.objects.get(id=id)
    khxoa=KhachHang.objects.get(username=adxoa.username)
    user = User.objects.get(username=adxoa.username)
    vttk=VaiTroTaiKhoan.objects.get(username=adxoa.username)
    user.delete()
    adxoa.delete()
    khxoa.delete()
    vttk.delete()

    return redirect("/quantrivien/pheduyet/quanlytaikhoankhachhang/xoa")
def viewQuanTriVienQuanLyVaiTro(request):
    vaitro = VaiTroTaiKhoan.objects.all()
    user=['']
    vaitrooj=['']
    for i in vaitro:
        user.append(i.username)
        if i.laquantrivien==1:
            vaitrooj.append('qtv')
        elif i.lakhachhang==1:
            print(i.username,"mất vai trò",i.lakhachhang)

            vaitrooj.append('kh')
        elif i.languoithamgiakhaosat==1:
            vaitrooj.append('ntgks')

        elif i.lanhanvienkinhdoanh==1:
            vaitrooj.append('nvkd')

    print(vaitrooj)

    if request.method == 'POST':
        vaitrorq=['']
        for i in vaitro:
            vaitrorq.append(request.POST.getlist(i.username)[0])
        for i in range(1,len(vaitrorq)):
            if vaitrorq[i]!=vaitrooj[i]:
                vaitroget = VaiTroTaiKhoan.objects.get(username=user[i])
                username=User.objects.get(username=user[i])
                print("khac",vaitrorq[i])
                if vaitrooj[i] == 'kh':
                    kh = KhachHang.objects.get(username=vaitroget.username)
                    kh.covaitro = 0
                    kh.save()
                if vaitrooj[i] == 'nvkd':
                    kh = NhanVienKinhDoanh.objects.get(username=vaitroget.username)
                    kh.covaitro = 0
                    kh.save()
                if vaitrooj[i] == 'ntgks':
                    kh = NguoiThamGiaKhaoSat.objects.get(username=vaitroget.username)
                    kh.covaitro = 0
                    kh.save()

                if vaitrorq[i]=='qtv':
                    vaitroget.lakhachhang = 0
                    vaitroget.languoithamgiakhaosat = 0
                    vaitroget.lanhanvienkinhdoanh = 0
                    vaitroget.laquantrivien = 1
                    vaitroget.save()
                a = QuanTriVien.objects.filter(username=vaitroget.username).count()
                if a == 0:
                    b = QuanTriVien()
                    b.username = vaitroget.username
                    b.email = username.email
                    b.covaitro = 1
                    b.save()
                elif vaitrorq[i]=='kh':
                    vaitroget.laquantrivien = 0
                    vaitroget.languoithamgiakhaosat = 0
                    vaitroget.lanhanvienkinhdoanh = 0
                    vaitroget.lakhachhang=1
                    vaitroget.save()
                    a=KhachHang.objects.filter(username=vaitroget.username).count()
                    if a==0:
                        b=KhachHang()
                        b.username=vaitroget.username
                        b.email = username.email
                        b.covaitro=1
                        b.save()
                    else:
                        b = KhachHang.objects.get(username=vaitroget.username)
                        b.email = username.email
                        b.covaitro = 1
                        b.save()
                elif vaitrorq[i]=='ntgks':
                    vaitroget.laquantrivien = 0
                    vaitroget.lakhachhang = 0
                    vaitroget.lanhanvienkinhdoanh = 0
                    vaitroget.languoithamgiakhaosat=1
                    vaitroget.save()
                    a=NguoiThamGiaKhaoSat.objects.filter(username=vaitroget.username).count()
                    if a==0:
                        b=NguoiThamGiaKhaoSat()
                        b.username=vaitroget.username
                        b.email=username.email
                        b.covaitro = 1
                        b.save()
                    else:
                        b = NguoiThamGiaKhaoSat.objects.get(username=vaitroget.username)
                        b.email = username.email
                        b.covaitro = 1
                        b.save()
                elif vaitrorq[i] == 'nvkd':
                    vaitroget.laquantrivien = 0
                    vaitroget.lakhachhang = 0
                    vaitroget.languoithamgiakhaosat = 0
                    vaitroget.lanhanvienkinhdoanh=1
                    vaitroget.save()
                    a=NhanVienKinhDoanh.objects.filter(username=vaitroget.username).count()
                    if a==0:
                        b=NhanVienKinhDoanh()
                        b.username=vaitroget.username
                        b.email = username.email
                        b.covaitro = 1
                        b.save()
                    else:
                        b = NhanVienKinhDoanh.objects.get(username=vaitroget.username)
                        b.email = username.email
                        b.covaitro = 1
                        b.save()
        vaitro = VaiTroTaiKhoan.objects.all()
        return render(request, 'quantrivien/quanlyvaitro.html', {'vaitro': vaitro})
    return render(request, 'quantrivien/quanlyvaitro.html',{'vaitro':vaitro})
def viewQuanTriVienQuanLyPhanQuyen(request):
    nvkd=NhanVienKinhDoanh.objects.filter(covaitro=1)
    if request.method == 'POST':
        for i in nvkd:
            nvkdget = NhanVienKinhDoanh.objects.get(username=i.username)
            list=request.POST.getlist(i.username)
            if len(list)==0:
                nvkdget.xemkhachhang = 0
                nvkdget.xoakhachhang = 0
                nvkdget.themkhachhang = 0
                nvkdget.suakhachhang = 0
                nvkdget.save()
            for i in range(0,len(list)):
                if 'xemkhachhang' in list:
                    nvkdget.xemkhachhang=1
                    nvkdget.save()
                else:
                    nvkdget.xemkhachhang=0
                    nvkdget.save()
                if 'themkhachhang' in list:
                    nvkdget.themkhachhang=1
                    nvkdget.save()
                else:
                    nvkdget.themkhachhang=0
                    nvkdget.save()
                if 'suakhachhang' in list:
                    nvkdget.suakhachhang=1
                    nvkdget.save()
                else:
                    nvkdget.suakhachhang=0
                    nvkdget.save()
                if 'xoakhachhang' in list:
                    nvkdget.xoakhachhang=1
                    nvkdget.save()
                else:
                    nvkdget.xoakhachhang=0
                    nvkdget.save()
        nvkd=NhanVienKinhDoanh.objects.filter(covaitro=1)
        return render(request, 'quantrivien/quanlyphanquyen.html', {'nvkd': nvkd})
    return render(request, 'quantrivien/quanlyphanquyen.html', {'nvkd': nvkd})
def viewNhanVienPheDuyetBaiKhaoSat(request):
    nvkd = NhanVienKinhDoanh.objects.get(username=request.user)
    khpheduyet=NhanVienPheDuyetBaiKhaoSat.objects.filter(nhanvienquanly__icontains=nvkd.manhanvien)
    return render(request, 'nhanvien/pheduyet/tongquanbaikhaosat.html',{'khpheduyet':khpheduyet})

#============================================Khảo sát============================================
def viewTaoCuocKhaoSat(request):
    khachhang = KhachHang.objects.get(username=request.user)
    if request.method == 'POST':
        dulieukhaosat=""
        for i in range(0,khachhang.socaukhaosat):
            dulieukhaosat=dulieukhaosat+"$None"
        for i in range(0,khachhang.soluongkhaosat):
            baikhaosat=BaiKhaoSat(username_khachhang=request.user,khaosatso=i,dulieukhaosat=dulieukhaosat[1:len(dulieukhaosat)])
            baikhaosat.save()
            khachhang.taocuockhaosat=True
            khachhang.save()
        return redirect("/khaosat/hienthidanhsach")

    return render(request, "khachhang/taocuockhaosat.html", {'sobai': khachhang.soluongkhaosat, 'socau': khachhang.socaukhaosat})
def viewHienThiBaiKhaoSat(request,id):
    baikhaosat = BaiKhaoSat.objects.get(Q(username_khachhang=request.user), Q(khaosatso=id))
    caukhaosat=baikhaosat.dulieukhaosat.split("$")
    cks=[]
    for i in range(0,len(caukhaosat)):
        cks.append([i,caukhaosat[i]])
    print(cks)
    count=NhanVienPheDuyetBaiKhaoSat.objects.filter(Q(username_khachhang=request.user), Q(khaosatso=id)).count()
    if count==1:
        msg="Chưa được phê duyệt"
    else:
        msg="Đã được phê duyệt"
    return render(request, "khaosat/baikhaosat/hienthi.html", {'caukhaosat': cks,'msg':msg,'id':id})
def viewSuaBaiKhaoSat(request,id1,id2):
    baikhaosat = BaiKhaoSat.objects.get(Q(username_khachhang=request.user), Q(khaosatso=id1))
    caukhaosat=baikhaosat.dulieukhaosat.split("$")
    cks=[]
    for i in range(0,len(caukhaosat)):
        cks.append([i,caukhaosat[i]])
    if request.method == 'POST':
        caukhaosat=baikhaosat.dulieukhaosat.replace(cks[id2][1],request.POST.getlist('cauhoi')[0],1)
        baikhaosat.dulieukhaosat=caukhaosat
        baikhaosat.save()
        count = NhanVienPheDuyetBaiKhaoSat.objects.filter(Q(username_khachhang=request.user), Q(khaosatso=id1)).count()
        if count==0:
            kh = KhachHang.objects.get(username=request.user)
            print("Thỏa mãn")
            if kh.nhanvienquanly=="":
                msg="Không thể sửa bài khảo sát do không tìm thấy nhân viên quản lý khách hàng này"
                return render(request, "khaosat/baikhaosat/hienthi.html", {'caukhaosat': cks,'msg':msg,'id':id1})
            adbks=NhanVienPheDuyetBaiKhaoSat(username_khachhang=request.user, khaosatso=id1,nhanvienquanly=kh.nhanvienquanly)
            adbks.save()
        return redirect("/khaosat/%d/baikhaosat/hienthi"%id1)
    return render(request, "khaosat/baikhaosat/sua.html", {'caukhaosat': cks[id2][1],'id':id1})
def viewBaiKhaoSatChoNguoiThamGia(request, id1, id2,tien, token):

    baikhaosat = BaiKhaoSat.objects.get(id=id2)
    caukhaosat = baikhaosat.dulieukhaosat.split("$")
    cks = []
    count = NguoiThamGiaKhaoSat.objects.filter(khaosat_token=token).count()
    if count==0:
        print(count)
        msg="Bạn đã hoàn thiện khảo sát này trước đó"
        return render(request, "khaosat/nguoithamgiakhaosat/trangthaithuchien.html",{'msg':msg})
    tgks=NguoiThamGiaKhaoSat.objects.get(khaosat_token=token)
    tennguoidung=tgks.username
    for i in range(0, len(caukhaosat)):
        cks.append([i, caukhaosat[i]])
    #câu trả lời trước
    cauhoi_traloi_truoc=tgks.ketquakhaosat
    #khởi tạo câu trả lời mới
    cauhoi_traloi=""
    if request.method == 'POST':
        for i in range(0,len(caukhaosat)):
            cauhoi_traloi=cauhoi_traloi+caukhaosat[i]+"$"+request.POST.getlist(str(i))[0]+"#"
        #ID+câu hỏi_câu trả lời+"&"
        cauhoi_traloi=str(id2)+"^"+cauhoi_traloi[0:len(cauhoi_traloi)-1]+"&"
        #câu hỏi_câu trả lời trước+câu hỏi_trả lời
        s=cauhoi_traloi_truoc+cauhoi_traloi
        tgks.ketquakhaosat=s
        #print(tgks.ketquakhaosat)
        tgks.khaosat_token=""
        tgks.tien=tgks.tien+tien
        tgks.save()
        msg="Chúc mừng "+tennguoidung+", bạn đã hoàn thành bài khảo sát, "+"Bạn nhận thêm được "+str(tien)\
            +". Tài khoản (tiền) hiện tại của bạn là "+str(tgks.tien)
        return render(request, "khaosat/nguoithamgiakhaosat/trangthaithuchien.html",{'msg':msg})
    return render(request, "khaosat/baikhaosat/lambaikhaosat.html", {'caukhaosat': cks, 'tennguoidung': tennguoidung})
def viewKhachHangXemKetQuaBaiKhaoSat(request, id1, id2):
    kqtgks = NguoiThamGiaKhaoSat.objects.get(id=id2)
    s=kqtgks.ketquakhaosat[0:len(kqtgks.ketquakhaosat)-1]
    s=s.split("&")
    data=[]
    dathuchien=False
    if len(kqtgks.ketquakhaosat) == 0:
        msg="Chưa thực hiện cuộc khảo sát nào"
        return render(request, "khaosat/nguoithamgiakhaosat/trangthaithuchien.html",{'msg':msg})
    for i in s:
        a=i.split("^")
        kqtgks = BaiKhaoSat.objects.get(id=int(a[0]))
        if kqtgks.username_khachhang==str(request.user) and kqtgks.khaosatso==id1:
            dathuchien=True
            b=a[1].split("#")
            for j in b:
                j=j.split("$")
                data.append([j[0],j[1]])
    if dathuchien==False:
        msg = "Khảo sát chưa được thực hiện bởi người tham gia"
        return render(request, "khaosat/nguoithamgiakhaosat/trangthaithuchien.html",{'msg':msg})
    return render(request, "khaosat/nguoithamgiakhaosat/ketqua.html",{'ketqua':data})
#========================================Nhân viên========================================================
def viewNhanVienXemBaiKhaoSat(request, id):
    nvpdbks = NhanVienPheDuyetBaiKhaoSat.objects.get(id=id)
    baikhaosat = BaiKhaoSat.objects.get(Q(username_khachhang=nvpdbks.username_khachhang), Q(khaosatso=nvpdbks.khaosatso))
    caukhaosat = baikhaosat.dulieukhaosat.split("$")
    cks = []
    for i in range(0, len(caukhaosat)):
        cks.append([i, caukhaosat[i]])
    return render(request, "nhanvien/pheduyet/chitietbaikhaosat.html",{'caukhaosat':cks})
def viewNhanVienDuyetBaiKhaoSat(request, id):
    nvpdbks = NhanVienPheDuyetBaiKhaoSat.objects.get(id=id)
    baikhaosat = BaiKhaoSat.objects.get(Q(username_khachhang=nvpdbks.username_khachhang), Q(khaosatso=nvpdbks.khaosatso))
    caukhaosat = baikhaosat.dulieukhaosat.split("$")
    cks = []
    for i in range(0, len(caukhaosat)):
        cks.append([i, caukhaosat[i]])
    return render(request, "nhanvien/pheduyet/chitietbaikhaosat.html",{'caukhaosat':cks})
def viewNhanVienPheDuyetKhaoSat(request, id):
    nvpdbks = NhanVienPheDuyetBaiKhaoSat.objects.get(id=id)
    nvpdbks.delete()
    return redirect("/nhanvien/pheduyet/hangdoikhaosat")
#========================================Người tham gia khảo sátt========================================================
def viewNguoiThamGiaKhaoSat(request):
    return render(request, "vaitro/nguoithamgiakhaosat.html")
def viewNguoiThamGiaKhaoSatXemSoDu(request):
    ntgks = NguoiThamGiaKhaoSat.objects.get(username=request.user)
    return render(request, "nguoithamgiakhaosat/sodu.html",{'tien':ntgks.tien})