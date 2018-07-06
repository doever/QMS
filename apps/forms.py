#!/usr/bin/python3
import json


class FormMixin(object):
    def get_errors(self):
        if hasattr(self,'errors'):
            errors = self.errors.as_json()   # json
            errors = json.loads(errors)
            print(errors)
            new_errors = {}
            for key,message_li in errors.items():
                messages = []
                for message in message_li:
                    messages.append(message['message'])
                new_errors[key] = messages
            return new_errors
        else:
            return {}

    # 取第一个错误
    def get_first_error(self):
        if hasattr(self, 'errors'):
            errors = self.errors.as_json()
            errors = json.loads(errors)
            # first_error = sorted(first_error_list[0].items())[1][1]

            key = list(errors.keys())[0]
            first_error = sorted(errors[key][0].items())[1][1]
            return first_error


# {'username': [{'message': '请输入用户名', 'code': 'required'}], 'nickname': [{'m
# essage': '请输入用户名', 'code': 'required'}], 'telephone': [{'message': 'This f
# ield is required.', 'code': 'required'}], 'password': [{'message': '请输入密码',
#  'code': 'required'}], 'email': [{'message': '请输入邮箱', 'code': 'required'}],
#  'birday': [{'message': 'This field is required.', 'code': 'required'}]}
# {'username': ['请输入用户名'], 'nickname': ['请输入用户名'], 'telephone': ['This
#  field is required.'], 'password': ['请输入密码'], 'email': ['请输入邮箱'], 'bir
# day': ['This field is required.']}
# {'username': [{'message': '请输入用户名', 'code': 'required'}], 'nickname': [{'m
# essage': '请输入用户名', 'code': 'required'}], 'telephone': [{'message': 'This f
# ield is required.', 'code': 'required'}], 'password': [{'message': '请输入密码',
#  'code': 'required'}], 'email': [{'message': '请输入邮箱', 'code': 'required'}],
#  'birday': [{'message': 'This field is required.', 'code': 'required'}]}

