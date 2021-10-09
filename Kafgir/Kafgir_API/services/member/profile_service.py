from dependency_injector.wiring import Provide, inject
from django.contrib.auth import get_user_model

from ...usecases.member.profile_usecase import ProfileUsecase
from ...dto.profile_dto import ProfileOutput, ProfileInput, ProfileSetPictureInput, ProfilePasswordChangeInput
from ...repositories.user_repo import UserRepository
from ...mappers.profile_mapper import ProfileOutputMapper
from ...exceptions.not_found import UserNotFoundException
from ...exceptions.bad_request import AuthenticationError, PasswordRepeatDidNotMatch

class ProfileService(ProfileUsecase):
    ''' This class is an implementation of profile usecase where every method goes to be an API for users to manage their own profiles'''

    @inject
    def __init__(self, user_repo: UserRepository = Provide['user_repo'],
                        profile_output_mapper: ProfileOutputMapper = Provide['profile_output_mapper']) -> None:
        self.user_repo = user_repo
        self.profile_output_mapper = profile_output_mapper
        super().__init__()
    
    model = get_user_model()

    def get_profile(self, id: int) -> ProfileOutput:
        ''' return user's profile details '''
        
        try:
            user = self.user_repo.get_user_by_id(id)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with (id={id}) was not found!')

        return self.profile_output_mapper.from_model(user)

    def change_password(self, id: int, input: ProfilePasswordChangeInput) -> None:
        ''' change user's password if the old password is entered correctly '''

        try:
            user = self.user_repo.get_user_by_id(id)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with (id={id}) was not found!')

        if not user.check_password(input.old_password):
            raise AuthenticationError()

        if input.new_password != input.new_password_rep:
            raise PasswordRepeatDidNotMatch()

        user.set_password(input.new_password)

        self.user_repo.save_user(user)


    def edit_profile(self, id: int, input: ProfileInput) -> ProfileOutput:
        ''' allow user edit his/her profile's detail '''

        try:
            user = self.user_repo.get_user_by_id(id)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with (id={id}) was not found!')

        user.name = input.name
        user.last_name = input.last_name

        self.user_repo.save_user(user)

        return self.profile_output_mapper.from_model(user)



    def set_photo(self, id: int, input: ProfileSetPictureInput) -> None:
        ''' allows user to set his/her profile picture '''

        try:
            user = self.user_repo.get_user_by_id(id)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with (id={id}) was not found!')

        user.image = input.image

        self.user_repo.save_user(user)

    def delete_photo(self, id: int) -> None:
        ''' allows user to delete his/her profile picture '''
        
        try:
            user = self.user_repo.get_user_by_id(id)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with (id={id}) was not found!')

        user.image.delete()

        self.user_repo.save_user(user)

    def logout(self, id: int) -> None:
        ''' logs out '''

        try:
            user = self.user_repo.get_user_by_id(id)
        except self.model.DoesNotExist:
            raise UserNotFoundException(detail=f'user with (id={id}) was not found!')

        user.auth_token.delete()

        self.user_repo.save_user(user)