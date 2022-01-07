from rest_framework.exceptions import APIException


class ValidatorException(APIException):
    """raises error with status_code, default_detail, default_code"""

    def __init__(self, default_detail, default_code, status_code):
        super(APIException, self).__init__()
        self.status_code = status_code
        self.default_detail = default_detail
        self.default_code = default_code
        self.detail = default_detail
