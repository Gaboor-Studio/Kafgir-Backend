import attr

from typing import Dict,get_args
from drf_yasg import openapi

def get_dto_structure(dto_class) -> Dict:
    '''This is a function for creating a dictionary containg the strcture of a dto class.
    It is used to create swagger responses.
    '''
    dic = dict()

    for f in attr.fields(dto_class):
        try:
            # For primitive types
            dic[f.name] = f.type()
        except:
            # Check if the object is list
            try:
                # For primitive types
                dic[f.name] = f.type()
            except:
                # Check if the object is generic
                if len(get_args(f.type)) != 0:
                    if f.type.__origin__ == list:
                        generic_type = get_args(f.type)[0]
                        
                        # Checking if the generic type is an attr class
                        if attr.has(generic_type):
                            strcuture = get_dto_structure(generic_type)
                            dic[f.name] = [strcuture]
                        else:
                            try:
                                dic[f.name] = [generic_type()]
                            except:
                                dic[f.name] = [str(generic_type)]
                else:
                    try:
                        if attr.has(f.type):
                            dic[f.name] = get_dto_structure(f.type)  
                        else:
                            dic[f.name] = str(f.type)
                    except:
                        dic[f.name] = str(f.type)
    
    return dic


def create_swagger_output(output_structure, description: str = '', many: bool = False, paginated: bool = False, content_type: str = 'application/json') -> Dict:
    '''This function is respnsible for creating responses for swagger auto schema.\n
    \n
    Parameters: \n
    output_structure: can be a dto class or a dictionary.\n
    \n
    Kwargs:\n
    description: a description for the api end point. default ''\n
    many: If you wanna output a list, you must set this parameter to True. default: False\n
    paginated: if you wanna paginate the result, you must set this parameter to True. default: False\n
    content_type: content type of the response. default: 'application/json'\n
    '''
    
    if output_structure is None:
        return {"200": openapi.Response(description=description, examples={content_type: None})}

    try:
        data = output_structure if output_structure is Dict else get_dto_structure(output_structure)

        if many:
            if paginated:
                return {"200": openapi.Response(description=description, examples={content_type: {'data': [data], 'total_pages': int(), 'current_page': int()}})}

            return {"200": openapi.Response(description=description, examples={content_type: [data]})}

        return {"200": openapi.Response(description=description, examples={content_type: data})}

    except:
        raise RuntimeError('output_structure must be a dto or a dictionary!')

    