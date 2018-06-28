# from django import forms
# from django.contrib.auth import get_user_model
# from django.contrib.auth import authenticate
# from django.core import validators
#
# class SigninForm(forms.ModelForm):
#     # username是唯一的,不能使用模型的username字段
#     username = forms.CharField(max_length=20)
#     class Meta:
#         model = get_user_model()
#         fields = ['password']
#         error_messages = {
#             'username':{
#                 'required':'请输入用户名',
#                 'invalid':'请输入有效的用户名'
#             }
#             # 'password':{
#                 # 'required': '请输入密码',
#             # }
#         }
#
#     def clean(self):
#         clean_data = super().clean()
#         username = clean_data.get('username')
#         password = clean_data.get('password')
#         user = authenticate(username=username,password=password)
#         # if user and user.is_active:
#         #     return clean_data
#         if not user:
#             raise forms.ValidationError(message='用户不存在,或密码错误')
#         elif not user.is_active:
#             raise forms.ValidationError(message='用户已被禁用')
#         else:
#             clean_data.update({"user":user})
#             return clean_data
