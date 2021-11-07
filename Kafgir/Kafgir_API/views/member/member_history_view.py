import attr
from dependency_injector.wiring import Provide, inject

from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status

from ...util.dto_util import create_swagger_output
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from typing import Any
import cattr

from ...dto.history_dto import HistoryOutput
from ...usecases.member.member_history_usecase import MemberHistoryUsecase

class MemberHistoryView(ViewSet):
    ''' This class is a view for users to be able to interact with their search history. '''

    @inject
    def __init__(self, member_history_usecase: MemberHistoryUsecase = Provide['member_history_usecase'], **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.member_history_usecase = member_history_usecase

    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(responses=create_swagger_output(HistoryOutput, many=True), tags=['member', 'history'],
                         manual_parameters=[openapi.Parameter('cnt', openapi.IN_QUERY, '# of history records to be returned.', required=False, type=openapi.TYPE_INTEGER)])
    def get_history(self, request):
        ''' This method returns a user's search history. '''
        cnt = request.query_params.get('cnt')
        outputs = self.member_history_usecase.get_history(request.user.id, cnt)
        serialized_outputs = list(map(attr.asdict, outputs))
        return Response(data=serialized_outputs, status=status.HTTP_200_OK)
    
    @swagger_auto_schema(responses=create_swagger_output(None), tags=['member', 'history'])
    def remove_history(self, request, hid=None):
        ''' This method removes a single record from user's history. '''
        self.member_history_usecase.remove_history(request.user.id, hid)
        return Response(data={'message': 'history was successfully removed!'}, status=status.HTTP_200_OK)

    @swagger_auto_schema(responses=create_swagger_output(None), tags=['member', 'history'])
    def clear_history(self, request):
        ''' This method clears a user's search history. '''
        self.member_history_usecase.remove_all_history(request.user.id)
        return Response(data={'message': 'history was successfully cleared!'}, status=status.HTTP_200_OK)
