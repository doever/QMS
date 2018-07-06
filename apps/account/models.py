from datetime import datetime

from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
from shortuuidfield import ShortUUIDField
from django.db import models


class UserManager(BaseUserManager):
    def _create_user(self,username,password,**kwargs):
        if not username:
            raise ValueError('请传入手机号码')
        if not password:
            raise ValueError('请传入密码')

        user = self.model(username=username,**kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_user(self,username,password,**kwargs):
        kwargs['is_superuser'] = False
        return self._create_user(username,password,**kwargs)

    def create_superuser(self,username,password,**kwargs):
        kwargs['is_superuser'] = True
        return self._create_user(username,password,**kwargs)


class User(AbstractBaseUser,PermissionsMixin):
    uid = ShortUUIDField(primary_key=True)
    username = models.CharField(max_length=50,unique=True)
    nickname = models.CharField(max_length=50,default='')
    telephone = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="userhead/%Y/%m",max_length=100,default='userhead/defalut.png')
    work_position = models.CharField(max_length=20,default='这个人很懒,什么都没有留下')
    jobs = models.CharField(max_length=20,default='员工')
    birday = models.DateTimeField(default=datetime.now)

    # 使用username验证
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['telephone']
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

