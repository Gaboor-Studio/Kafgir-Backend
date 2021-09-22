import inspect

from ..exceptions.common import ValidationError

def validate(serializer_class):
    '''
        This is a decorator for data validation. 
        You can use this decorator on the top of the view methods to perform data validation.
    '''
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Finding value of 'request' parameter
            args_name = inspect.getfullargspec(func)[0]
            args_dict = dict(zip(args_name, args))
            request = args_dict['request']

            #Perform validation
            seri = serializer_class(data=request.data)
            if seri.is_valid():
                return func(*args, **kwargs)
            raise ValidationError(detail=seri.errors)
        return wrapper
    return decorator