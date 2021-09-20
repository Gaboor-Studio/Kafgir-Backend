from typing import List

from ...dto.admin_management_dto import AdminOutput, AdminRegisterInput, AdminSetPasswordInput, AdminBriefOutput
from ...repositories.user_repo import UserRepository
from ...mappers.admin_management_mapper import AdminBriefMapper,AdminMapper
from ...exceptions.not_found import AdminNotFoundException
from ...usecases.admin.admin_management_usecases import AdminManagementUsecase

from dependency_injector.wiring import Provide, inject

from django.contrib.auth import get_user_model

user_model = get_user_model()

class AdminManagementService(AdminManagementUsecase):

    @inject
    def __init__(self, user_repo: UserRepository = Provide['user_repo'],
                       admin_mapper: AdminMapper = Provide['admin_mapper'],
                       admin_brief_mapper: AdminBriefMapper = Provide['admin_brief_mapper']):
        self.user_repo = user_repo
        self.admin_mapper = admin_mapper
        self.admin_brief_mapper=  admin_brief_mapper

    def find_admin(self, id: int) -> AdminOutput:
        ''' Finds an admin by id.'''

        try:
            user = self.user_repo.get_user_by_id_and_is_staff(id, True)
            return self.admin_mapper.from_model(user)
        except user_model.DoesNotExist:
            raise AdminNotFoundException(detail=f'Admin(id= {id}) not found!')

    def load_all_admins(self) -> List[AdminBriefOutput]:
        '''Returns a list of admins containing brief outputs.'''

        admins = self.user_repo.get_all_by_is_staff(True)
        return list(map(self.admin_brief_mapper.from_model, list(admins)))

    def delete_admin(self, id: int) -> None:
        '''Deletes an admin by id.'''

        try:
            self.user_repo.get_user_by_id_and_is_staff(id, True)
            self.user_repo.delete_by_id(id)
        except user_model.DoesNotExist:
            raise AdminNotFoundException(detail=f'Admin(id= {id}) not found!')

    def create_admin(self, input: AdminRegisterInput) -> AdminOutput:
        ''' Creates an admin.'''
        
        if not self.user_repo.exist_user_by_username(input.username):
            if not self.user_repo.exist_user_by_username(input.email):
                user = user_model.objects.create_superuser(username=input.username, email=input.email, name=input.name,
                                               last_name=input.last_name, password=input.password, is_superuser=input.is_superuser)
                self.user_repo.save_user(user)
                return self.admin_mapper.from_model(user)

            raise AdminNotFoundException(detail=f'Admin(email= {input.email}) not found!')

        raise AdminNotFoundException(detail=f'Admin(username= {input.username}) not found!')

    def update_admin(self, id: int, input: AdminRegisterInput) -> AdminOutput:
        ''' Updates an admin.'''
        try:
            user = self.user_repo.get_user_by_id_and_is_staff(id, True)
            
            user.username = input.username
            user.email = input.email
            user.name = input.name
            user.last_name = input.last_name
            user.is_superuser = input.is_super_admin

            self.user_repo.save_user(user)
            return self.admin_mapper.from_model(user)
        
        except user_model.DoesNotExist:
            raise AdminNotFoundException(detail=f'Admin(id= {id}) not found!')

    def set_password(self, id: int, input: AdminSetPasswordInput) -> None:
        '''Sets admin's password given his/her id and new password.'''

        try:
            user = self.user_repo.get_user_by_id_and_is_staff(id, True)
            user.set_password(input.new_password)
            self.user_repo.save_user(user)
        except user_model.DoesNotExist:
            raise AdminNotFoundException(detail=f'Admin(id= {id}) not found!')
