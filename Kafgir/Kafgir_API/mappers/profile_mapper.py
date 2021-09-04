from django.contrib.auth import get_user_model
from ..dto.profile_dto import ProfileOutput

class ProfileOutputMapper:

    user_model = get_user_model()

    def from_model(self, model: user_model):

        if model == None:
            return None

        return ProfileOutput(username= model.username,
                             email=model.email,
                             name=model.name,
                             last_name=model.last_name,
                             image=model.image
                            )