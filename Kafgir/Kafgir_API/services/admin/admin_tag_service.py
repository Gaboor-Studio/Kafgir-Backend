from typing import List

from ...dto.tag_dto import TagInput, TagOutput, SetTagImageInput
from ...usecases.admin.admin_tag_usecases import AdminTagUsecase
from ...repositories.tag_repo import TagRepository
from ...mappers.tag_mapper import TagMapper
from ...models.tag import Tag
from ...exceptions.not_found import TagNotFoundException

from dependency_injector.wiring import inject, Provide

class AdminTagServices(AdminTagUsecase):
    ''' This class is an abstract class for usecases of admin_tag api '''

    @inject
    def __init__(self, tag_repo: TagRepository = Provide['tag_repo'],
                       tag_mapper: TagMapper = Provide['tag_mapper']
                       ):
        self.tag_repo = tag_repo
        self.tag_mapper = tag_mapper
        

    def find_all(self) -> List[TagOutput]:
        ''' This method returns a list of all tags .'''

        return list(map(self.tag_mapper.from_model, self.tag_repo.find_all()))

    def find_by_id(self, id: int) -> TagOutput:
        ''' Finds a tag by id.'''

        try:
            tag = self.tag_repo.find_by_id(id)
            return self.tag_mapper.from_model(tag)
        except Tag.DoesNotExist:
            raise TagNotFoundException(detail=f'tag(id={id}) not found!') 

    def create_new_tag(self, input:  TagInput) -> None:
        '''creates a tag .'''
        if input.image == None :
            tag = Tag(title=input.title, is_main=input.is_main, is_primary=input.is_primary, display_order=input.display_order)
        else :
            tag = Tag(title=input.title, is_main=input.is_main, is_primary=input.is_primary, display_order=input.display_order, image=input.image)
        self.tag_repo.save(tag)

    def update_tag(self, id: int, input:  TagInput) -> None:
        '''updates a Tag .'''

        try:
            tag = self.tag_repo.find_by_id(id)
            
            tag.title = input.title
            tag.is_main = input.is_main
            tag.is_primary = input.is_primary
            tag.display_order = input.display_order
            
            if not input.image == None :
                tag.image = input.image

            self.tag_repo.save(tag)
        
        except Tag.DoesNotExist:
            raise TagNotFoundException(detail=f'tag(id={id}) not found!') 

    def set_tag_image(self, id: int, input:  SetTagImageInput) -> None:
        ''' This method sets image for a tag'''
        
        try:
            tag = self.tag_repo.find_by_id(id)
            
            tag.image = input.image

            self.tag_repo.save(tag)
        
        except Tag.DoesNotExist:
            raise TagNotFoundException(detail=f'tag(id={id}) not found!')
    
    def remove_tag(self, id: int) -> None:
        ''' deletes a tag by ID.'''

        self.tag_repo.delete_by_id(id)
