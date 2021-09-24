from dependency_injector.wiring import Provide, inject
from typing import List
from django.contrib.auth import get_user_model

from ...exceptions.bad_request import UserAlreadyExistsException
from ...exceptions.not_found import UserNotFoundException
from ...usecases.admin.user_management_usecases import UserManagementUsecase
from ...mappers.user_management_mapper import UserManagementProfileMapper
from ...repositories.user_repo import UserRepository
from ...dto.user_management_dto import UserManagementEditProfileInput, UserManagementCreateProfileInput \
                                     , UserManagementSetPasswordInput, UserManagementSetPfpInput \
                                     , UserManagementProfileOutput

class UserManagementService(UserManagementUsecase):
    ''' This class is an abstract class for usecases of user-management api '''

    @inject
    def __init__(self, user_repo: UserRepository = Provide['user_repo'], 
                    user_management_profile_mapper: UserManagementProfileMapper = \
                        Provide['user_management_profile_mapper']) -> None:
        super().__init__()
        self.user_repo = user_repo
        self.user_management_profile_mapper = user_management_profile_mapper

    user_model = get_user_model()
    
    def get_users_list(self) -> List[UserManagementProfileOutput]:
        ''' This method returns a list of users that are not admins'''
        return list(map(self.user_management_profile_mapper.from_model, self.user_repo.get_all_by_is_staff(False)))

    
    def create_user(self, input: UserManagementCreateProfileInput) -> UserManagementProfileOutput:
        ''' Using this method, you can create a new user to the system and activate it at the same time'''
        if self.user_repo.exist_user_by_username(input.username):
            raise UserAlreadyExistsException(detail=f'User(username={input.username}) already exists!')           

        if self.user_repo.exist_user_by_email(input.email):
            raise UserAlreadyExistsException(detail=f'User(email={input.email}) already exists!')

        user = self.user_model.objects.create_user(
            username=input.username, email=input.email, name=input.name, last_name=input.last_name, password=input.password)
        
        user.is_active = input.is_active.lower() == 'true'

        self.user_repo.save_user(user)

        return self.user_management_profile_mapper.from_model(user)

    
    def edit_user(self, id: int, input: UserManagementEditProfileInput) -> UserManagementProfileOutput:
        ''' This method is used to edit a user's profile'''
        try: 
            user = self.user_repo.get_user_by_id_and_is_staff(id, False)
        except self.user_model.DoesNotExist:
            raise UserNotFoundException(f'User(id={id}) does not exist!')

        if input.username != user.username:
            if self.user_repo.exist_user_by_username(input.username):
                raise UserAlreadyExistsException(detail=f'User(username={input.username}) already exists!') 
            user.username= input.username
        
        user.name= input.name
        user.last_name= input.last_name
        user.is_active= input.is_active.lower() == 'true'

        self.user_repo.save_user(user)  

        return self.user_management_profile_mapper.from_model(user)

    
    def delete_user(self, id:int) -> None:
        ''' Deletes the user with pk of given id'''
        try: 
            user = self.user_repo.get_user_by_id_and_is_staff(id, False)
        except self.user_model.DoesNotExist:
            raise UserNotFoundException(f'User(id={id}) does not exist!')

        user.delete()

    def set_user_password(self, id: int, input: UserManagementSetPasswordInput) -> None:
        ''' This method sets the password for a user'''        
        try: 
            user = self.user_repo.get_user_by_id_and_is_staff(id, False)
            user.set_password(input.new_password)
            self.user_repo.save_user(user)
        except self.user_model.DoesNotExist:
            raise UserNotFoundException(f'User(id={id}) does not exist!')
 
    def set_user_pfp(self, id: int, input: UserManagementSetPfpInput) -> None:
        ''' This method sets pfp for a user'''
        try: 
            user = self.user_repo.get_user_by_id_and_is_staff(id, False)
            user.image = input.image
            self.user_repo.save_user(user)
        except self.user_model.DoesNotExist:
            raise UserNotFoundException(f'User(id={id}) does not exist!')
