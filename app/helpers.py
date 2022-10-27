from django.core.mail import send_mail
from django.conf import settings 


def guiMailDatLaiMatKhau(email, token):
    subject = 'Link đặt lại mật khẩu'
    message = f'Xin chào, để đặt lại mật khẩu bạn vui lòng click vào link sau: http://127.0.0.1:8000/datlaimatkhau/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
def guiMailToiNguoiThamGiaKhaoSat(email, token,id1,id2,tien):
    subject = 'Link thực hiện khảo sát'
    message = f'Xin chào, để thực hiện bài khảo sát bạn vui lòng click vào link sau: http://127.0.0.1:8000/khaosat/{id1}/baichonguoithamgia/{id2}/{tien}/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True
