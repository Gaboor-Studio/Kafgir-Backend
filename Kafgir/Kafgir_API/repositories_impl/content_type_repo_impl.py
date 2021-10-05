from ..repositories.content_type_repo import ContentTypeRepository

from django.contrib.contenttypes.models import ContentType

class ContentTypeRepositoryImpl(ContentTypeRepository):

    def find_content_type_by_model(self, model):
        return ContentType.objects.get_for_model(model)