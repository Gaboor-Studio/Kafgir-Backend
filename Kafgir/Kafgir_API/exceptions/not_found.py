from rest_framework.exceptions import APIException

class ShoppingListItemNotFoundException(APIException):
    status_code = 404
    default_detail = 'shopping list item not found!'
    default_code = 'not_found'

class UserNotFoundException(APIException):
    status_code = 404
    default_detail = 'user not found!'
    default_code = 'not_found'

class FoodPlanNotFoundException(APIException):
    status_code = 404
    default_detail = 'food plan not found!'
    default_code = 'not_found'

class FoodNotFoundException(APIException):
    status_code = 404
    default_detail = 'food not found!'
    default_code = 'not_found'

class TagNotFoundException(APIException):
    status_code = 404
    default_detail = 'tag not found!'
    default_code = 'not_found'

class IngredientNotFoundException(APIException):
    status_code = 404
    default_detail = 'ingredient not found!'
    default_code = 'not_found'

class CommentNotFoundException(APIException):
    status_code = 404
    default_detail = 'comment not found!'
    default_code = 'not_found'

class AdminNotFoundException(APIException):
    status_code = 404
    default_detail = 'admin not found!'
    default_code = 'not_found'