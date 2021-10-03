from time import time

from .models import Logger


class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/'):
            t_start = time()
            response = self.get_response(request)
            execution_time = time() - t_start
            Logger.objects.create(
                method=request.method,
                path=request.path,
                execution_time=execution_time
            )
            return response
        else:
            response = self.get_response(request)
            return response
