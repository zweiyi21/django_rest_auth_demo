from django.utils.deprecation import MiddlewareMixin
import json


class JsonRequestMiddleware(MiddlewareMixin):
    def process_request(self, request):
        try:
            if request.content_type == "application/x-www-form-urlencoded":
                data = json.loads(request.body)

                request.json_data = data
        except ValueError:
            pass
