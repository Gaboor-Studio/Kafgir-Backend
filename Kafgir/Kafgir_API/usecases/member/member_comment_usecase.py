from abc import ABC, abstractmethod

from ...dto.comment_dto import CommentBriefInput

class MemberCommentUsecase(ABC):
    '''This is an abstraction for member comment service.
    
    It provides some functionalities such as updating comments and removing comments ...
    '''
    
    @abstractmethod
    def update_comment(self, comment_id: int, input:  CommentBriefInput) -> None:
        '''Updates the comment of the user.'''
        pass

    @abstractmethod
    def remove_comment(self, comment_id: int) -> None:
        '''Removes the comment of the user.'''
        pass