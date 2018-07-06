# -*- coding: utf-8 -*-
from random import Random

from django.core.mail import send_mail
from django.core.cache import cache

from QMS.settings import EMAIL_FROM


def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str


def send_reset_email(email):
    code = random_str(6)
    cache.set(email,code,60*5)
    email_title = "OZNER密码重置"
    email_body = "亲爱的用户:%s" % email+", 您的验证码为:%s" % code
    send_mail(email_title, email_body, EMAIL_FROM, [email])
    # return send_status,code



