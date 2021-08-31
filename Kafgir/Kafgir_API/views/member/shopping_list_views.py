from dependency_injector.wiring import inject, Provide
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import cattr
from typing import List

from ...usecases.member.shopping_list_usecases import MemberShoppingListUsecase
from ...serializers.shopping_list_serializer import ShopingListInputSerializer
from ...dto.shopping_list_dto import ShoppingListItemOutput, ShoppingListItemInput


class MemberShoppingListView(ViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    shopping_list_serializer = ShopingListInputSerializer

    @inject
    def __init__(self, member_shopping_list_usecase: MemberShoppingListUsecase = Provide['member_shopping_list_usecase']):
        self.member_shopping_list_usecase = member_shopping_list_usecase

    def get_shopping_list(self, request):
        outputs = self.member_shopping_list_usecase.find_shopping_list(request.user.id)
        serialized_outputs = list(map(cattr.unstructure, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)
    
    def create_new_shopping_list_item(self, request):
        seri = self.shopping_list_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, ShoppingListItemInput)
            output = self.member_shopping_list_usecase.add_new_shopping_list_item(input=input,user=request.user)
            serialized_output = cattr.unstructure(output)
            return Response(data=serialized_output, status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    def create_new_shopping_list(self, request):
        seri = self.shopping_list_serializer(data=request.data, many=True)
        if seri.is_valid():
            input = cattr.structure(request.data, List[ShoppingListItemInput])
            self.member_shopping_list_usecase.add_new_shopping_list(inputs=input,user=request.user)
            return Response(status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    def update_shopping_list_item(self, request, item_id=None):
        seri = self.shopping_list_serializer(data=request.data)
        if seri.is_valid():
            input = cattr.structure(request.data, ShoppingListItemInput)
            self.member_shopping_list_usecase.update_shopping_list_item(item_id=item_id, input=input)
            return Response(status=status.HTTP_200_OK)
        return Response(data={'error': 'Invalid data!', 'err': seri.errors}, status=status.HTTP_400_BAD_REQUEST)

    def done(self, request, item_id=None):
        self.member_shopping_list_usecase.done(item_id)
        return Response(data={}, status=status.HTTP_200_OK)        

    def undone(self, request, item_id=None):
        self.member_shopping_list_usecase.undone(item_id)
        return Response(data={}, status=status.HTTP_200_OK)

    def remove_shopping_list_item(self, request, item_id=None):
        self.member_shopping_list_usecase.remove_shopping_list_item(item_id)
        return Response(data={}, status=status.HTTP_200_OK)
    