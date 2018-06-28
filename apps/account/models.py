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
    telephone = models.CharField(max_length=11,unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    data_joined = models.DateTimeField(auto_now_add=True)

    # 使用username验证
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['telephone']
    EMAIL_FIELD = 'email'

    objects = UserManager()

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username