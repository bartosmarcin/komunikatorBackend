from django.http import HttpResponse
import json
import datetime

def jsonDef(o):
    if isinstance(o, set):
        return list(o)
    if isinstance(o, datetime.datetime) or isinstance(o, datetime.date):
        return o.isoformat()
    return o.__dict__


class ServiceResponse:
    def __init__(self, response):
        self.response = response
        self.isSuccess = True
        self.errors = []

    def to_json(self):
        return json.dumps(self, default=jsonDef)
    
    def to_http_response(self):
        return HttpResponse(self.to_json())

    def addError(self, error, isCritical=True):
        self.errors.append(error)
        if isCritical:
            self.isSuccess = False

MIN_PASSWORD_LEN = 8
MAX_PASSWORD_LEN = 60
