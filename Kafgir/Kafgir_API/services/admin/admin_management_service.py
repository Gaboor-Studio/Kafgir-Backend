from typing import List

from django.core import exceptions

from ...dto.admin_management_dto import AdminOutput, AdminRegisterInput, AdminSetPasswordInput, AdminBriefOutput, AdminUpdateProfileInput
from ...repositories.user_repo import UserRepository
from ...mappers.admin_management_mapper import AdminBriefMapper,AdminMapper
from ...exceptions.not_found import AdminNotFoundException, PageNotFoundException
from ...exceptions.bad_request import UserAlreadyExistsException
from ...usecases.admin.admin_management_usecases import AdminManagementUsecase
from ...util.paginator import PaginationData,PaginatorUtil

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

    def load_all_admins(self, pagination_data: PaginationData) -> List[AdminBriefOutput]:
        '''Returns a list of admins containing brief outputs.'''

        admins = self.user_repo.get_all_by_is_staff(True)
        try:
            paginated_admins, pages = PaginatorUtil.paginate_query_set(admins, pagination_data)
            data = list(map(self.admin_brief_mapper.from_model, paginated_admins))
            return PaginatorUtil.create_pagination_output(data, pages, pagination_data.page)
        except:
            raise PageNotFoundException(detail= f'Page({pagination_data.page}) not found!')

    def delete_admin(self, id: int) -> None:
        '''Deletes an admin by id.'''

        try:
            self.user_repo.get_user_by_id_and_is_staff(id, True)
            self.user_repo.delete_by_id(id)
        except user_model.DoesNotExist:
            raise AdminNotFoundException(detail=f'Admin(id= {id}) not found!')

    def create_admin(self, input: AdminRegisterInput) -> AdminOutput:
        ''' Creates an admin.'''
        
        if self.user_repo.exist_user_by_username(input.username):
            raise UserAlreadyExistsException(detail=f'A user already exists with the username({input.username})')
        
        if self.user_repo.exist_user_by_email(input.email):
            raise UserAlreadyExistsException(detail=f'A user already exists with the email({input.email})')
        
        user = user_model.objects.create_superuser(username=input.username, email=input.email, name=input.name,
                                            last_name=input.last_name, password=input.password, is_superuser=input.is_superuser)
        self.user_repo.save_user(user)
        return self.admin_mapper.from_model(user)

        

    def update_admin(self, id: int, input: AdminUpdateProfileInput) -> AdminOutput:
        ''' Updates an admin.'''
        try:
            user = self.user_repo.get_user_by_id_and_is_staff(id, True)

            if user.username != input.username:
                if self.user_repo.exist_user_by_username(input.username):
                    raise UserAlreadyExistsException(detail=f'A user already exists with the username({input.username})')
                user.username = input.username

            if user.email != input.email:
                if self.user_repo.exist_user_by_email(input.email):                
                    raise UserAlreadyExistsException(detail=f'A user already exists with the email({input.email})')
                user.email = input.email

            user.name = input.name
            user.last_name = input.last_name
            user.is_superuser = input.is_superuser

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
