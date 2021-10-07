from abc import ABC,abstractmethod

class CrudRepository(ABC):

    @abstractmethod
    def find_by_id(self, id: int, model_class):
        pass

    @abstractmethod
    def save(self, model):
        pass

    @abstractmethod
    def delete_by_id(self, id: int, model_class):
        pass
    