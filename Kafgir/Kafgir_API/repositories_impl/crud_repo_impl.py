from ..repositories.crud_repo import CrudRepository

class CrudRepositoryImpl(CrudRepository):

    def find_by_id(self, id: int, model_class):
        return model_class.objects.get(pk=id)

    def save(self, model):
        model.save()

    def delete_by_id(self, id: int, model_class):
        model_class.objects.filter(pk=id).delete()
    