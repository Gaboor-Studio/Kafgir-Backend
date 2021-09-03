import attr

from typing import Dict
from drf_yasg import openapi

def get_dto_structure(dto_class) -> Dict:
    dic = dict()

    for f in attr.fields(dto_class):
        try:
            dic[f.name] = f.type()
        except:
            dic[f.name] = str(f.type)
    
    return dic


def dto_to_swagger_json_output(dto_class, description: str = '', many=False) -> Dict:
    if dto_class is None:
        return {"200": openapi.Response(description=description, examples={"application/json": None})}
    if many:
        return {"200": openapi.Response(description=description, examples={"application/json": [get_dto_structure(dto_class)]})}

    return {"200": openapi.Response(description=description, examples={"application/json": get_dto_structure(dto_class)})}
