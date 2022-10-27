from django import forms
from .service import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
#===========================Đăng ký===============================================
class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("username","email")
class SignUpForm(UserCreationForm):
    username = models.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(max_length=100)
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if len(password1)<8:
                raise forms.ValidationError("Độ dài mật khẩu tối thiểu phải là 8 ký tự")
            if matKhauThoaManDinhDangQuyUoc(password1)==False:
                raise forms.ValidationError\
                    ("Mật khẩu đăng ký không đúng định dạng (phải bao gồm: chữ hoa,chữ thường,số, ký tự đặc biệt")
            if password1 == password2 and password1:
                return password2
    def clean_email(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            if emailThoaManDinhDangQuyUoc(email) == False:
                raise forms.ValidationError("Email không đúng định dạng")
            else:
                return email
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user



#===========================Đổi mật khẩu===============================================
class SetPasswordForm(forms.Form):
    new_password1 = forms.CharField(widget=forms.PasswordInput())
    new_password2 = forms.CharField(widget=forms.PasswordInput())
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)
    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if len(password1) < 8:
                raise forms.ValidationError("Độ dài mật khẩu tối thiểu phải là 8 ký tự")
            elif matKhauThoaManDinhDangQuyUoc(password1) == False:
                raise forms.ValidationError\
                    ("Mật khẩu mới không đúng định dạng (phải bao gồm: chữ hoa,chữ thường,số, ký tự đặc biệt")
            elif password1 != password2:
                raise forms.ValidationError("Mật khẩu không khớp")
        return password2
    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user
class PasswordChangeForm(SetPasswordForm):
    old_password = forms.CharField(widget=forms.PasswordInput())
    def clean_old_password(self):
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError("Mật khẩu cũ không đúng")
        return old_password
#===========================Khách hàng===============================================

class KhachHangForm(forms.ModelForm):
    class Meta:
        model = KhachHang
        fields = ("username","makhachhang","hoten","email","diachi","sodienthoai"
        ,"madinhdanh","motanoidungyeucau","giatien","soluongkhaosat","socaukhaosat","kichhoat")
class QuanTriVienPheDuyetKhachHangThemForm(forms.ModelForm):
    class Meta:
        model = HangDoiQuanTriVienPheDuyet
        fields = '__all__'

#===========================Người tham gia khảo sát===============================================
class NguoiThamGiaKhaoSatForm(forms.ModelForm):
    class Meta:
        model = NguoiThamGiaKhaoSat
        fields = ("username","email","sodienthoai","thongtinkhac")
class SignUpForm(UserCreationForm):
    username = models.CharField(max_length=100)
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())
    email = forms.CharField(max_length=100)
    def clean_password2(self):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if len(password1)<8:
                raise forms.ValidationError("Độ dài mật khẩu tối thiểu phải là 8 ký tự")
            if matKhauThoaManDinhDangQuyUoc(password1)==False:
                raise forms.ValidationError\
                    ("Mật khẩu đăng ký không đúng định dạng (phải bao gồm: chữ hoa,chữ thường,số, ký tự đặc biệt")
            if password1 == password2 and password1:
                return password2
    def clean_email(self):
        if 'email' in self.cleaned_data:
            email = self.cleaned_data['email']
            if emailThoaManDinhDangQuyUoc(email) == False:
                raise forms.ValidationError("Email không đúng định dạng")
            else:
                return email
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user