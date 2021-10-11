from Kafgir_API.repositories.user_repo import UserRepository
from dependency_injector.wiring import inject, Provide

from ...models.comment import Comment
from ...models.food import Food

from ...usecases.admin.admin_comment_usecases import AdminCommentUsecase
from ...dto.comment_dto import CommentInput,CommentIdListInput,CommentOutput
from ...repositories.comment_repo import CommentRepository
from ...repositories.food_repo import FoodRepository
from ...repositories.crud_repo import CrudRepository
from ...mappers.comment_mapper import CommentMapper,CommentBriefMapper
from ...exceptions.not_found import CommentNotFoundException,FoodNotFoundException
from ...util.paginator import PaginationData,PaginationOutput,PaginatorUtil

from typing import List

class AdminCommentService(AdminCommentUsecase):
    ''' This class is an abstract class for usecases of admin_comment api '''

    @inject
    def __init__(self, comment_repo: CommentRepository = Provide['comment_repo'],
                       food_repo: FoodRepository = Provide['food_repo'],
                       comment_mapper: CommentMapper = Provide['comment_mapper'],
                       comment_brief_mapper: CommentBriefMapper = Provide['comment_brief_mapper'],
                       crud_repo: CrudRepository = Provide['crud_repo']):

        self.comment_repo = comment_repo
        self.food_repo = food_repo
        self.comment_mapper = comment_mapper
        self.comment_brief_mapper = comment_brief_mapper
        self.crud_repo = crud_repo

    def get_comment(self, comment_id: int) -> CommentOutput:
        '''This method returns a comment given its id.'''
        try:
            comment = self.comment_repo.find_by_id(comment_id)
            return self.comment_mapper.from_model(comment)
        except Comment.DoesNotExist:
            raise CommentNotFoundException(detail=f'Comment(id = {comment_id}) not found!')

    def get_comments_by_confirmed(self, confirmed: bool, pagination_data: PaginationData) -> PaginationOutput:
        '''This method returns a list of paginated comments with respect to confirmed field.'''
        # Get all confirmed/unconfirmed comments
        comments = self.comment_repo.find_all_by_confirmed_ordered_by_datetime_desc(confirmed=confirmed)

        # Create paginated data
        paginated_comments, pages = PaginatorUtil.paginate_query_set(comments, pagination_data)
        data = list(map(self.comment_brief_mapper.from_model, paginated_comments))
        return PaginatorUtil.create_pagination_output(data, pages, pagination_data.page)
 
    def confirm_the_comment(self, comment_id: int) -> None:
        '''This method receives a comment ID to confirm user comment .'''
        try:
            comment = self.comment_repo.find_by_id(comment_id)
            
            # update model ratings
            model = comment.content_object
            model.rating = ((model.rating * model.rating_count) + comment.rating) / (model.rating_count + 1)
            model.rating_count += 1
            self.crud_repo.save(model)
            
            comment.confirmed = True
            self.comment_repo.save(comment)
        
        except Comment.DoesNotExist:
            raise CommentNotFoundException(
                detail=f'comment with comment_id={comment_id} does not exist!')
 
    def confirm_comments(self, comments: CommentIdListInput) -> None:
        '''This method receives a list of comment IDs for confirming user comments .'''
        for comment_id in comments.commentid_list:
            try:
                comment = self.comment_repo.find_by_id(comment_id)
                    
                comment.confirmed = True

                self.comment_repo.save(comment)
            
            except Comment.DoesNotExist:
                raise CommentNotFoundException(
                    detail=f'comment with comment_id={comment_id} does not exist!')


    def update_comment(self, comment_id: int, input:  CommentInput) -> None:
        '''updates a comment .'''
        try:
            comment = self.comment_repo.find_by_id(comment_id)

            #update commantable model
            if comment.confirmed:
                model = comment.content_object
                model.rating -= comment.rating / model.rating_count
                model.rating_count -= 1
                self.crud_repo.save(model)

            comment.rating = input.rating
            comment.text = input.text           
            comment.confirmed = False

            self.comment_repo(comment)
        
        except Comment.DoesNotExist:
            raise CommentNotFoundException(
                detail=f'comment with comment_id={comment_id} does not exist!')

    def remove_comment(self, comment_id: int) -> None:
        '''deletes a comment by ID.'''
        # Check if comment exists
        try:
            comment = self.comment_repo.find_by_id(comment_id)
            
            # Update commentable rating if the comment was confirmed
            if comment.confirmed:
                model = comment.content_object
                model.rating = ((model.rating * model.rating_count) - comment.rating) / (model.rating_count - 1) if model.rating_count != 1 else 0
                model.rating_count -= 1
                self.crud_repo.save(model)

            # Delete comment
            self.comment_repo.delete_by_id(comment_id)
        except Comment.DoesNotExist:
            raise CommentNotFoundException(
                detail=f'comment with comment_id={comment_id} does not exist!')
