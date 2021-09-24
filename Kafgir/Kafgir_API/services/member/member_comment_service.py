from ...dto.comment_dto import CommentBriefInput
from ...usecases.member.member_comment_usecase import MemberCommentUsecase
from ...models.comment import Comment
from ...repositories.comment_repo import CommentRepository
from ...exceptions.not_found import CommentNotFoundException,FoodNotFoundException

from dependency_injector.wiring import inject, Provide

class MemberCommentService(MemberCommentUsecase):
    '''This is an implementation of the MemberCommentUsecase.
    It provides the services needed for comment in the client side.
    '''
    
    @inject
    def __init__(self, comment_repo: CommentRepository = Provide['comment_repo']):
        
        '''Constructor with 1 argument which is dependency of this service. This is automatically injected by the framework'''
        
        self.comment_repo = comment_repo

    def update_comment(self, comment_id: int, input:  CommentBriefInput) -> None:
        '''Updates the comment of the user.'''
        try:
            comment = self.comment_repo.find_by_id(comment_id)
            
            comment.rating = input.rating
            comment.text = input.text           
            comment.confirmed = False

            comment.save()
        
        except Comment.DoesNotExist:
            raise CommentNotFoundException(
                detail=f'comment with comment_id={comment_id} does not exist!')

    def remove_comment(self, comment_id: int) -> None:
        '''Removes the comment of the user.'''
        self.comment_repo.delete_by_id(comment_id)