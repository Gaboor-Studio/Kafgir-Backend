from rest_framework.exceptions import APIException

class UserAlreadyExistsException(APIException):
    status_code = 400
    default_detail = 'A user with this email already exists!'
    default_code = 'bad_request'

class CannotUseOldPasswordException(APIException):
    status_code = 400
    default_detail = 'new password cannot be the same as the old one!'
    default_code = 'bad_request'


class AuthenticationError(APIException):
    status_code = 400
    default_detail = 'old password did not match your password!'
    default_code = 'bad_request'

class UserIsNotAdmin(APIException):
    status_code = 400
    default_detail = 'the user with the id you provided is not among admins. this section belongs to admins only!'
    default_code = 'bad_request'

class UserIsAdmin(APIException):
    status_code = 400
    default_detail = 'the user with the id you provided is an admin. this section belongs to non-admins only!'
    default_code = 'bad_request'