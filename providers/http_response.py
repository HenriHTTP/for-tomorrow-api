class HttpResponse:
    def __init__(self, success, message, error, status_code):
        self.success = success
        self.message = message
        self.error = error
        self.status_code = status_code
