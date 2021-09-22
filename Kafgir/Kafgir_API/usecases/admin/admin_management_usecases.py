from abc import ABC, abstractmethod

from typing import List

from ...dto.admin_management_dto import AdminOutput, AdminRegisterInput, AdminSetPasswordInput, AdminBriefOutput, AdminUpdateProfileInput
from ...util.paginator import PaginationData

class AdminManagementUsecase(ABC):
    '''This class is an abstraction for admin managment services.
    This use cases are used in admin panel to manage admins.
    '''

    @abstractmethod
    def find_admin(self, id: int) -> AdminOutput:
        ''' Finds an admin by id.'''
        pass

    @abstractmethod
    def load_all_admins(self, pagination_data: PaginationData) -> List[AdminBriefOutput]:
        '''Returns a list of admins containing brief outputs.'''
        pass

    @abstractmethod
    def delete_admin(self, id: int) -> None:
        '''Deletes an admin by id.'''
        pass

    @abstractmethod
    def create_admin(self, input: AdminRegisterInput) -> AdminOutput:
        ''' Creates an admin.'''
        pass

    @abstractmethod
    def update_admin(self, id: int, input: AdminUpdateProfileInput) -> AdminOutput:
        ''' Updates an admin.'''
        pass

    @abstractmethod
    def set_password(self, id: int, input: AdminSetPasswordInput) -> None:
        '''Sets admin's password given his/her id and new password.'''
        pass
