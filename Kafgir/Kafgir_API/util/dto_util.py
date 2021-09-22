import attr

from typing import Dict
from drf_yasg import openapi

def get_dto_structure(dto_class) -> Dict:
    '''This is a function for creating a dictionary containg the strcture of a dto class.
    It is used to create swagger responses.
    '''
    dic = dict()

    for f in attr.fields(dto_class):
        try:
            dic[f.name] = f.type()
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

    