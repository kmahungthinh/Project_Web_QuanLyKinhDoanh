import hashlib
from django.contrib.auth.models import User
from .models import *
def string_To_List_PhanTuTrongListLaString(Str,soKyTuTai1PhanTuList):
  listTemp=[]
  x=0
  for i in range(0,int(len(Str)/soKyTuTai1PhanTuList)):
    listTemp.append(Str[x:x+soKyTuTai1PhanTuList])
    x=x+soKyTuTai1PhanTuList
  return listTemp
alphabetHoa=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"
    ,"Q","R","S","T","U","V","W","X","Y","Z"]
alphabetThuong=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o"
    ,"p","q","r","s","t","u","v","w","x","y","z"]
So=["0","1","2","3","4","5","6","7","8","9"]
kyTuDacBiet=["!","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";"
    ,"<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~","\,","\""]

def matKhauThoaManDinhDangQuyUoc(matkhau):
    coHoa = False
    coThuong = False
    coSo = False
    coKyTuDacBiet = False
    for i in range(0,len(matkhau)):
        if matkhau[i] in alphabetHoa:
            coHoa=True
    for i in range(0, len(matkhau)):
        if matkhau[i] in alphabetThuong:
            coThuong = True
    for i in range(0, len(matkhau)):
        if matkhau[i] in kyTuDacBiet:
            coKyTuDacBiet = True
    for i in range(0, len(matkhau)):
        if matkhau[i] in So:
            coSo = True
    if (coHoa==True) and (coThuong==True) and (coHoa==True) and (coKyTuDacBiet==True) and (coSo==True):
        return True
    return False
def emailThoaManDinhDangQuyUoc(email):
    listEmail=string_To_List_PhanTuTrongListLaString(email,1)
    if "@" in listEmail:
        return True
    else:
        return False
def sdtThoaManDinhDangQuyUoc(sdt):
    if len(sdt)!=10:
        return False
    listSDT=string_To_List_PhanTuTrongListLaString(sdt,1)
    for i in listSDT:
        if i not in So:
            return False
    return True

def sv_capNhatKhachHang(id,datacapnhat):
    kh = KhachHang.objects.get(id=id)
    user = User.objects.get(username=kh.username)

    kh.makhachhang=datacapnhat[2]
    kh.hoten=datacapnhat[3]
    kh.diachi = datacapnhat[4]
    kh.sodienthoai = datacapnhat[5]
    kh.madinhdanh=datacapnhat[6]
    kh.email = datacapnhat[7]
    kh.motanoidungyeucau=datacapnhat[8]
    kh.giatien=datacapnhat[9]
    kh.soluongkhaosat=datacapnhat[10]
    kh.socaukhaosat=datacapnhat[11]
    kh.kichhoat=datacapnhat[12]
    kh.save()

    user.username = datacapnhat[0]
    user.set_password(datacapnhat[1])
    user.email = datacapnhat[7]
    user.save()
def sv_themKhachHang(datathem):
    kh = KhachHang()
    user = User()
    kh.username=datathem[0]
    kh.makhachhang=datathem[2]
    kh.hoten=datathem[3]
    kh.diachi = datathem[4]
    kh.sodienthoai = datathem[5]
    kh.madinhdanh=datathem[6]
    kh.email = datathem[7]
    kh.motanoidungyeucau=datathem[8]
    kh.giatien=datathem[9]
    kh.soluongkhaosat=datathem[10]
    kh.socaukhaosat=datathem[11]
    kh.kichhoat=datathem[12]
    kh.covaitro=1
    kh.save()

    kh = KhachHang.objects.get(username=kh.username)
    kh.covaitro = 1
    kh.save()

    user.username = datathem[0]
    user.set_password(datathem[1])

    user.save()
def CreateAccount(tendangnhap, email, matkhau):
    user = User.objects.create_user(tendangnhap, email, matkhau)
    user.save()
def sv_capNhatNguoiThamGiaKhaoSat(id,datacapnhat):

    tgks = NguoiThamGiaKhaoSat.objects.get(id=id)
    user = User.objects.get(username=tgks.username)

    tgks.username = datacapnhat[0]
    tgks.sodienthoai = datacapnhat[2]
    tgks.email=datacapnhat[3]
    tgks.thongtinkhac=datacapnhat[4]
    tgks.save()

    user.username = datacapnhat[0]
    user.set_password(datacapnhat[1])
    user.email=datacapnhat[3]
    user.save()





