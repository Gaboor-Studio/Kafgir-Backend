from django.contrib.auth import get_user_model
from ..dto.profile_dto import ProfileOutput

class ProfileOutputMapper:
    ''' This mapper class has all tools to map a user model to a ProfileOutput dto'''

    user_model = get_user_model()

    def from_model(self, model: user_model):
        ''' this method maps a use model to a ProfileOutput dto'''

        if model == None:
            return None

        return ProfileOutput(username= model.username,
                             email=model.email,
                             name=model.name,
                             last_name=model.last_name,
                             image=model.get_image()
                            )