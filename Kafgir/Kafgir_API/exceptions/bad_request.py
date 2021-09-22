from rest_framework.exceptions import APIException

class UserAlreadyExistsException(APIException):
    status_code = 400
    default_detail = 'A user with this email already exists!'
    default_code = 'bad_request'

class CannotUseOldPasswordException(APIException):
    status_code = 400
    default_detail = 'new password cannot be the same as the old one!'
    default_code = 'bad_request'

class PasswordRepeatDidNotMatch(APIException):
    status_code = 400
    default_detail = 'the password and it\'s repeat does not match'
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

class OptPasswordIsntSet(APIException):
    status_code = 400
    default_detail = 'user has not requested for a email confirmation code yet'
    default_code = 'bad_request'

class UserIsAlreadyActivated(APIException):
    status_code = 400
    default_detail = 'user is already activated!'
    default_code = 'bad_request'

class PasscodeIsExpired(APIException):
    status_code = 400
    default_detail = 'your passcode is already expired!'
    default_code = 'bad_request'

class WrongPasscode(APIException):
    status_code = 400
    default_detail = 'your entered passcode is wrong!'
    default_code = 'bad_request'

class ResetTokenIsNotSet(APIException):
    status_code = 400
    default_detail = 'user has not requested for a token yet'
    default_code = 'bad_request'

class ResetTokenIsExpired(APIException):
    status_code = 400
    default_detail = 'your reset token is already expired!'
    default_code = 'bad_request'

class WrongResetToken(APIException):
    status_code = 400
    default_detail = 'your entered reset token is wrong!'
    default_code = 'bad_request'

class SearchFieldMissing(APIException):
    status_code = 400
    default_detail = 'a required field is missing in your request'
    default_code = 'bad_request'

class TagIdMissingException(APIException):
    status_code = 400
    default_detail = 'You must send tag id to get foods.'
    default_code = 'bad_request'
