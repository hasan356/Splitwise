import json
from decimal import Decimal


def parse_request_body(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    return body


class decimal_encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        return json.JSONEncoder.default(self, obj)