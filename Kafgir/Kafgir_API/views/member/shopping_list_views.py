from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import cattr
from typing import List

from ...usecases.member.shopping_list_usecases import MemberShoppingListUsecase
from ...serializers.shopping_list_serializer import ShopingListInputSerializer, CreateShopingListInputSerializer
from ...dto.shopping_list_dto import ShoppingListItemOutput, ShoppingListItemInput, ShoppingListItemBriefInput

from drf_yasg.utils import swagger_auto_schema
from typing import List
import attr
from ...util.dto_util import dto_to_swagger_json_output

class MemberShoppingListView(ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    shopping_list_serializer = ShopingListInputSerializer
    create_shopping_list_serializer = CreateShopingListInputSerializer

    @inject
    def __init__(self, member_shopping_list_usecase: MemberShoppingListUsecase = Provide['member_shopping_list_usecase']):
        self.member_shopping_list_usecase = member_shopping_list_usecase

    @swagger_auto_schema(responses=dto_to_swagger_json_output(ShoppingListItemOutput, many=True), tags=['member','shopping-list'])
    def get_shopping_list(self, request):
        ''' Gets user shopping list.'''
        
        outputs = self.member_shopping_list_usecase.find_shopping_list(request.user.id)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=create_shopping_list_serializer, responses=dto_to_swagger_json_output(None), tags=['member','shopping-list']) 
    def create_new_shopping_list_item(self, request):
        ''' Creates new shopping list item.'''

        seri = self.create_shopping_list_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, ShoppingListItemBriefInput)
            output = self.member_shopping_list_usecase.add_new_shopping_list_item(input=input,user=request.user)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=create_shopping_list_serializer(many=True), responses=dto_to_swagger_json_output(None), tags=['member','shopping-list'])
    def create_new_shopping_list(self, request):
        ''' Adds all items to the shopping list.'''

        seri = self.create_shopping_list_serializer(data=request.data, many=True)
        if seri.is_valid():
            input = cattr.structure(request.data, List[ShoppingListItemBriefInput])
            self.member_shopping_list_usecase.add_new_shopping_list(inputs=input,user=request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=shopping_list_serializer, responses=dto_to_swagger_json_output(None), tags=['member','shopping-list'])
    def update_shopping_list_item(self, request, item_id=None):
        ''' Updates a shopping list item.'''

        seri = self.shopping_list_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, ShoppingListItemInput)
            self.member_shopping_list_usecase.update_shopping_list_item(item_id=item_id, input=input)
            return Response(status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)


    @swagger_auto_schema(responses=dto_to_swagger_json_output(None), tags=['member','shopping-list'])
    def done(self, request, item_id=None):
        ''' Sets a shopping list item to done status.'''

        self.member_shopping_list_usecase.done(item_id)
        return Response(data=None, status=status.HTTP_200_OK)        

    @swagger_auto_schema(responses=dto_to_swagger_json_output(None), tags=['member','shopping-list'])
    def undone(self, request, item_id=None):
        ''' Sets a shopping list item to undone status.'''

        self.member_shopping_list_usecase.undone(item_id)
        return Response(data=None, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=dto_to_swagger_json_output(None), tags=['member','shopping-list'])
    def remove_shopping_list_item(self, request, item_id=None):
        ''' Removes a shopping list item from the shopping list.'''

        self.member_shopping_list_usecase.remove_shopping_list_item(item_id)
        return Response(data=None, status=status.HTTP_200_OK)
    
