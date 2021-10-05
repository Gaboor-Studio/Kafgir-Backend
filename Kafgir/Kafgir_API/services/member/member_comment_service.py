from ...repositories.content_type_repo import ContentTypeRepository
from ...dto.comment_dto import CommentOutput, CommentInput
from ...usecases.member.member_comment_usecase import MemberCommentUsecase
from ...models.comment import Comment, Commentable
from ...repositories.comment_repo import CommentRepository
from ...repositories.crud_repo import CrudRepository
from ...repositories.content_type_repo import ContentTypeRepository
from ...exceptions.not_found import CommentNotFoundException,PageNotFoundException
from ...exceptions.bad_request import CommentAlreadyExists
from ...util.paginator import PaginatorUtil,PaginationData,PaginationOutput
from ...mappers.comment_mapper import CommentMapper,MyCommentMapper

from django.contrib.auth import get_user_model
from django.core.paginator import EmptyPage

from dependency_injector.wiring import inject, Provide

user_model = get_user_model()

class MemberCommentService(MemberCommentUsecase):
    '''This is an implementation of the MemberCommentUsecase.
    It provides the services needed for comment in the client side.
    '''
    
    @inject
    def __init__(self, comment_repo: CommentRepository = Provide['comment_repo'], \
                content_type_repo: ContentTypeRepository = Provide['content_type_repo'], \
                crud_repo: CrudRepository = Provide['crud_repo'],
                comment_mapper: CommentMapper = Provide['comment_mapper']):
        '''Constructor with arguments which are dependencies of this service. This is automatically injected by the framework'''
        self.comment_repo = comment_repo
        self.content_type_repo = content_type_repo
        self.crud_repo = crud_repo
        self.comment_mapper = comment_mapper

    def update_comment(self, comment_id: int, input: CommentInput) -> None:
        '''Updates the comment of the user.'''
        # Check if comment exists
        try:
            comment = self.comment_repo.find_by_id(comment_id)

            # update commantable model
            if comment.confirmed:
                model = comment.content_object
                model.rating -= comment.rating / model.rating_count
                model.rating_count -= 1
                self.crud_repo.save(model)

            # update comment
            comment.rating = input.rating
            comment.text = input.text           
            comment.confirmed = False
            self.comment_repo.save(comment)
        
        except Comment.DoesNotExist:
            raise CommentNotFoundException(
                detail=f'comment with comment_id={comment_id} does not exist!')

    def remove_comment(self, comment_id: int) -> None:
        '''Removes the comment of the user.'''
        # Check if comment exists
        try:
            comment = self.comment_repo.find_by_id(comment_id)
            
            # Update commentable rating is the comment was confirmed
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
    
    def get_all_comments_of_model(self, model_class: Commentable, model_id: int, pagination_data: PaginationData, confirmed = True) -> PaginationOutput:
        '''Gets all comments of a model given its id and returns PaginationOutput.'''
        # Checking if the model exists
        try:
            model = self.crud_repo.find_by_id(model_id, model_class)

            # Get corresponding content type. it uses cached data, so it will not hit database twice for a model.
            content_type = self.content_type_repo.find_content_type_by_model(model_class)

            # Get confirmed comments    
            comments = self.comment_repo.find_all_by_confirmed_and_model_order_by_datetime_desc \
                (obj_id=model_id, content_type=content_type, confirmed=confirmed)

            # Paginate comments
            try:
                paginated_comments, pages = PaginatorUtil.paginate_query_set(comments, pagination_data)

                # Convert paginated comments to comment output
                data = list(map(self.comment_mapper.from_model, paginated_comments))

                # Create pagination output
                return PaginatorUtil.create_pagination_output(data, pages, pagination_data.page)

            except EmptyPage:
                raise PageNotFoundException(detail= f'Page({pagination_data.page}) not found!')
        except model_class.DoesNotExist:
            raise CommentNotFoundException(detail=f'{model_class.__name__}(id={model_id}) not found!') 

    def find_comment_by_user_id(self, user_id: int, model_class: Commentable, model_id: int) -> CommentOutput:
        '''Finds the user comment on the post if exists.'''
        try:
            model = self.crud_repo.find_by_id(model_id, model_class)
            
            # Get corresponding content type. it uses cached data, so it will not hit database twice for a model.
            content_type = self.content_type_repo.find_content_type_by_model(model_class)
            
            try:
                comment = self.comment_repo.find_by_user_id_and_model(user_id=user_id, obj_id=model_id, content_type=content_type)
                return self.comment_mapper.from_model(comment)
            except Comment.DoesNotExist:
                return None
        except model_class.DoesNotExist:
            raise CommentNotFoundException(detail=f'{model_class.__name__}(id={model_id}) not found!') 

    def add_comment(self, model_class: Commentable, model_id: int, user: user_model, input:  CommentInput) -> None:
        '''Posts a comment on the model with the given user.'''
        try:
            model = self.crud_repo.find_by_id(model_id, model_class)

            # Get corresponding content type. it uses cached data, so it will not hit database twice for a model.
            content_type = self.content_type_repo.find_content_type_by_model(model_class)

            # Create comment if user has not commented before
            if not self.comment_repo.exist_by_user_id_and_model(user_id=user.id, obj_id=model_id, content_type=content_type):
                self.comment_repo.create(model, user, input.text, input.rating)

            else:
                raise CommentAlreadyExists(detail='A comment already exist!')

            #TODO: else throw an error
        except model_class.DoesNotExist:
            raise CommentNotFoundException(detail=f'{model_class.__name__}(id={model_id}) not found!') 