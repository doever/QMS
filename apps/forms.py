#!/usr/bin/python3
import json

class FormMixin(object):
    def get_errors(self):
        if hasattr(self,'errors'):
            errors = self.errors.as_json()   # json
            errors=json.loads(errors)
            new_errors = {}
            for key,message_li in errors.items():
                messages=[]
                for message in message_li:
                    messages.append(message['message'])
                new_errors[key]=messages
            return new_errors
        else:
            return {}


