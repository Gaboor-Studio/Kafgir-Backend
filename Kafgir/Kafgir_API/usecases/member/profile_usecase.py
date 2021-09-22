from abc import ABC, abstractmethod
from ...dto.profile_dto import ProfileInput, ProfileSetEmailInput, ProfileSetPictureInput, ProfilePasswordChangeInput, ProfileOutput

class ProfileUsecase(ABC):
    ''' This class is an abstract class defining usecases of profile API'''

    @abstractmethod
    def get_profile(self, id: int) -> ProfileOutput:
        ''' return user's profile details '''
        pass

    @abstractmethod
    def change_password(self, id: int, input: ProfilePasswordChangeInput) -> None:
        ''' change user's password if the old password is entered correctly '''
        pass

    @abstractmethod
    def edit_profile(self, id: int, input: ProfileInput) -> ProfileOutput:
        ''' allow user edit his/her profile's detail '''
        pass

    @abstractmethod
    def set_photo(self, id: int, input: ProfileSetPictureInput) -> None:
        ''' allows user to set his/her profile picture '''
        pass

    @abstractmethod
    def logout(self, id: int) -> None:
        ''' logs out '''
        pass