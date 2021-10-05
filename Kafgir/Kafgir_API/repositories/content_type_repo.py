from abc import ABC,abstractmethod

class ContentTypeRepository(ABC):

    @abstractmethod
    def find_content_type_by_model(self, model):
        pass