from ..dto.user_management_dto import UserManagementProfileOutput

from django.contrib.auth import get_user_model

user_model = get_user_model()

class UserManagementProfileMapper():
    ''' This mapper class maps a user model to a usermanagement output dto'''

    def from_model(self, model: user_model) -> UserManagementProfileOutput:
        ''' This method maps a user model to a usermanagement output dto'''

        if model == None:
            return None

        return UserManagementProfileOutput(id=model.pk,
                                            username=model.username,
                                            email=model.email,
                                            name=model.name,
                                            last_name=model.last_name,
                                            image=model.get_image(),
                                            is_active=model.is_active)