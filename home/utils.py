from rest_framework.response import Response

class CORSResponse(Response):
    def __init__(self, *args, **kwargs):
        headers = kwargs.pop('headers', {})
        headers['Access-Control-Allow-Origin'] = '*'
        super().__init__(*args, **kwargs, headers=headers)
