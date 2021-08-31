from rest_framework.exceptions import APIException



class ValidationError(APIException):
    status_code = 400
    default_detail = 'Invalid request body!'
    default_code = 'bad_request'
