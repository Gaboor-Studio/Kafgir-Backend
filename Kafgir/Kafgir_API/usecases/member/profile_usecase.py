from abc import ABC, abstractmethod
from ...dto.profile_dto import ProfileInput, ProfileSetEmailInput, ProfileSetPictureInput, ProfilePasswordChangeInput, ProfileOutput

class ProfileUsecase(ABC):

    @abstractmethod
    def get_profile(self, id: int) -> ProfileOutput:
        pass

    @abstractmethod
    def change_password(self, id: int, input: ProfilePasswordChangeInput) -> None:
        pass

    @abstractmethod
    def edit_profile(self, id: int, input: ProfileInput) -> ProfileOutput:
        pass

    @abstractmethod
    def set_photo(self, id: int, input: ProfileSetPictureInput) -> None:
        pass