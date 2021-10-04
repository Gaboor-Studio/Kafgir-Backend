from dependency_injector.wiring import Provide, inject

from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from typing import Any
import cattr

from ...usecases.member.member_history_usecase import MemberHistoryUsecase

class MemberHistoryView(ViewSet):
    ''' This class is a view for users to be able to interact with their search history. '''

    @inject
    def __init__(self, member_history_usecase: MemberHistoryUsecase = Provide['member_history_usecase'], **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.member_history_usecase = member_history_usecase

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    def get_history(self, request):
        ''' This method returns a user's search history. '''
        output = self.member_history_usecase.get_history(request.user.id)
        serialized_output = cattr.unstructure(output)
        return Response(data=serialized_output, status=status.HTTP_200_OK)
    
    def remove_history(self, request, hid=None):
        ''' This method removes a single record from user's history. '''
        self.member_history_usecase.remove_history(hid)
        return Response(data={'message': 'history was successfully removed!'}, status=status.HTTP_200_OK)
