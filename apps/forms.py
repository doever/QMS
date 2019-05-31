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


