# -*- coding: utf-8 -*-
__author__ = 'caiqinxiong_cai'
#2020/3/3 10:01
import threading
from django.core.mail import  send_mail, send_mass_mail, EmailMultiAlternatives
from django.template import loader
from django.conf import settings
import os,django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "SCM.settings")# project_name 项目名称
# django.setup()

class SendMail(threading.Thread):
    def __init__(self,subject, message, from_email, recipient_list, fail_silently=False, html_message=None):
        self.subject = subject # 邮件标题
        self.message = message # 邮件txt内容
        self.html_message = html_message # HTML邮件
        self.from_email = from_email # 发件人
        self.recipient_list = [recipient_list] # 收件人列表
        self.fail_silently = fail_silently # 如果失败，是否抛出错误
        threading.Thread.__init__(self) # 继承多线程父类

    def run(self):# 重写run方法
        status_code = send_mail(self.subject,self.message,self.from_email,self.recipient_list,self.fail_silently)
        print(status_code)
        return status_code

    def html_mail(self,mail_temp):
        '''发送HTML邮件'''
        email_template_name = mail_temp
        t = loader.get_template(email_template_name)
        html_content = t.render(self.message)
        msg = EmailMultiAlternatives(self.subject, html_content, self.from_email,self.recipient_list)
        msg.attach_alternative(html_content, "text/html")
        msg.send()

# smail = SendMail('mail test',# 邮件标题
#               'test6',# 邮件txt内容
#               'caiqinxiong_cai@qq.com',# 发件人
#               ['caiqinxiong_cai@qq.com','caiqinxiong_cai@easou.cn'])# 收件人列表
# smail.start()


#
# def smail(request):
#     '''发送邮件'''
#     status_code = send_mail('mail test',
#               'test',
#               'caiqinxiong_cai@qq.com',
#               ['caiqinxiong_cai@qq.com','caiqinxiong_cai@easou.cn'],
#                 fail_silently = False)
#     # 值1：邮件标题   值2：邮件主人  值3：发件人  值4：收件人  值5：如果失败，是否抛出错误
#     print(status_code)
#     if status_code == 1:
#         return HttpResponse('邮件发送成功')
#     else:
#         return HttpResponse('邮件发送失败')