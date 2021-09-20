from ..dto.admin_management_dto import AdminBriefOutput, AdminOutput, AdminUpdateProfileInput

from django.contrib.auth import get_user_model

user_model = get_user_model()


class AdminBriefMapper:
    ''' This is a mapper for converting user default model to AdminBriefOutput DTO'''

    def from_model(self, model: get_user_model) -> AdminBriefOutput:
        '''Takes a model of user and converts it to AdminBriefOutput DTO'''

        if model == None:
            return None

        return AdminBriefOutput(id=model.pk, username=model.username, name=model.name, last_name=model.last_name)


class AdminMapper:
    ''' This is a mapper for converting user default model to AdminBriefOutput DTO'''

    def from_model(self, model: get_user_model) -> AdminOutput:
        '''Takes a model of user and converts it to AdminOutput DTO'''

        if model == None:
            return None

        return AdminOutput(id=model.pk, username=model.username, name=model.name, last_name=model.last_name,
                           email=model.email, is_superuser=model.is_superuser)
