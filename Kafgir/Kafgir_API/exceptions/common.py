from rest_framework.exceptions import APIException

class ValidationError(APIException):
    status_code = 400
    default_detail = 'Invalid request body!'
    default_code = 'bad_request'

class CannotGetCurrentTime(APIException):
    status_code = 400
    default_detail = 'there was a problem getting the current time'

class CannotGenerateCode(APIException):
    status_code = 400
    default_detail = 'there was a problem generating a new passcode'

class CannotSendEmail(APIException):
    status_code = 400
    default_detail = 'there was a problem sending the email'

class CannotGenerateToken(APIException):
    status_code = 400
    default_detail = 'there was a problem generating a token for you!'