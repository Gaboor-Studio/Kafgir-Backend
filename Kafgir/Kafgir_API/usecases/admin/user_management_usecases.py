from abc import ABC, abstractmethod
from typing import List

from ...dto.user_management_dto import UserManagementEditProfileInput, UserManagementCreateProfileInput \
                                     , UserManagementSetPasswordInput, UserManagementSetPfpInput \
                                     , UserManagementProfileOutput

class UserManagementUsecase(ABC):
    ''' This class is an abstract class for usecases of user-management api '''

    @abstractmethod
    def get_users_list(self) -> List[UserManagementProfileOutput]:
        ''' This method returns a list of users that are not admins'''
        pass

    @abstractmethod
    def create_user(self, input: UserManagementCreateProfileInput) -> UserManagementProfileOutput:
        ''' Using this method, you can create a new user to the system and activate it at the same time'''
        pass

    @abstractmethod
    def edit_user(self, id: int, input: UserManagementEditProfileInput) -> UserManagementProfileOutput:
        ''' This method is used to edit a user's profile'''
        pass

    @abstractmethod
    def delete_user(self, id:int) -> None:
        ''' Deletes the user with pk of given id'''
        pass

    @abstractmethod
    def set_user_password(self, id: int, input: UserManagementSetPasswordInput) -> None:
        ''' This method sets the password for a user'''
        pass

    @abstractmethod
    def set_user_pfp(self, id: int, input: UserManagementSetPfpInput) -> None:
        ''' This method sets pfp for a user'''
        pass

    @abstractmethod
    def delete_user_pfp(self, id: int) -> None:
        ''' This method deletes pfp for a usre'''
        pass
