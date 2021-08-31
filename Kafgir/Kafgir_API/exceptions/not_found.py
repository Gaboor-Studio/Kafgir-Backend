from rest_framework.exceptions import APIException

class ShoppingListItemNotFoundException(APIException):
    status_code = 404
    default_detail = 'shopping list item not found!'
    default_code = 'not_found'

class UserNotFoundException(APIException):
    status_code = 404
    default_detail = 'user not found!'
    default_code = 'not_found'