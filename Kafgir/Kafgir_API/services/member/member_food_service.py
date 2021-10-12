from typing import List

from ...dto.food_dto import FoodBriefOutput
from ...usecases.member.member_food_usecase import MemberFoodUsecase
from ...models.food import Food
from ...models.comment import Comment
from ...models.user import User
from ...models.shopping_list_item import ShoppingListItem
from ...models.tag import Tag
from ...exceptions.not_found import FoodNotFoundException,TagNotFoundException,PageNotFoundException, UserNotFoundException
from ...repositories.food_repo import FoodRepository
from ...repositories.tag_repo import TagRepository
from ...repositories.shopping_list_repo import ShoppingListRepository
from ...repositories.user_repo import UserRepository
from ...repositories.comment_repo import CommentRepository
from ...repositories.content_type_repo import ContentTypeRepository
from ...mappers.food_mappers import FoodMapper
from ...mappers.comment_mapper import CommentMapper,MyCommentMapper
from ...exceptions.not_found import FoodNotFoundException
from ...mappers.food_mappers import FoodMapper,FoodBriefMapper
from ...util.paginator import PaginationData,PaginationOutput, PaginatorUtil

from django.contrib.auth import get_user_model
from dependency_injector.wiring import inject, Provide

class MemberFoodService(MemberFoodUsecase):
    '''This is an implementation of the MemberFoodUsecase.
    It provides the services needed for foods in the client side.
    '''
    
    user_model = get_user_model()

    @inject
    def __init__(self, food_repo: FoodRepository = Provide['food_repo'],
                       tag_repo: TagRepository = Provide['tag_repo'],
                       food_mapper: FoodMapper = Provide['food_mapper'],
                       shopping_list_repo: ShoppingListRepository = Provide['shopping_list_repo'],
                       comment_repo: CommentRepository = Provide['comment_repo'],
                       user_repo: UserRepository = Provide['user_repo'],
                       comment_mapper: CommentMapper = Provide['comment_mapper'],
                       food_brief_mapper: FoodBriefMapper = Provide['food_brief_mapper'],
                       content_type_repo: ContentTypeRepository = Provide['content_type_repo'],
                       my_comment_mapper: MyCommentMapper = Provide['my_comment_mapper']):
        '''Constructor with arguments which are dependencies of this service. They are automatically injected by the framework'''
        self.tag_repo = tag_repo
        self.food_repo = food_repo
        self.food_mapper = food_mapper
        self.food_brief_mapper = food_brief_mapper
        self.shopping_list_repo = shopping_list_repo
        self.comment_repo = comment_repo
        self.user_repo = user_repo
        self.comment_mapper = comment_mapper
        self.content_type_repo = content_type_repo
        self.my_comment_mapper = my_comment_mapper

    def find_by_id(self, user_id: int, food_id: int, pagination_data: PaginationData) -> PaginationOutput:
        '''Finds a food given its id and returns a PaginationOutput containing paginated comments.'''
        #Checking if the food exists
        try:
            food = self.food_repo.find_by_id(food_id)
            food_output = self.food_mapper.from_model(food)

            # Find content_type
            content_type = self.content_type_repo.find_content_type_by_model(food)

            # Checking if we have a current logged in user
            if user_id:
                # Finding user comments on the food
                try:
                    my_comment = self.comment_repo.find_by_user_id_and_model(user_id, food.id, content_type)
                    if not my_comment==None:
                        food_output.my_comment = self.my_comment_mapper.from_model(my_comment)
                except Comment.DoesNotExist:
                    pass    

            # Get confirmed comments    
            comments = self.comment_repo.find_all_by_confirmed_and_model_order_by_datetime_desc(food.id, content_type)

            # Paginate comments
            try:
                paginated_comments, pages = PaginatorUtil.paginate_query_set(comments, pagination_data)

                # Convert paginated comments to comment output
                data = list(map(self.comment_mapper.from_model, paginated_comments))

                # Create pagination output
                food_output.comments = PaginatorUtil.create_pagination_output(data, pages, pagination_data.page)

                return food_output
            except:
                raise PageNotFoundException(detail= f'Page({pagination_data.page}) not found!')

        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={id}) not found!')

    def add_ingredients_to_list(self, food_id: int, user: user_model) -> None:
        ''''Adds all food's ingredients to the user's shopping list.'''
        # Checking if the food exists
        try:
            food = self.food_repo.find_by_id(food_id)

            # Adding food ingredients to the user's shopping list
            for ingredient in food.ingredient_pieces.all():
                item = ShoppingListItem(title=ingredient.ingredient.name, amount=ingredient.amount, user=user)
                self.shopping_list_repo.save_item(item)
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={id}) not found!')

    def find_all_with_tag(self, tag_id: int, pagination_data: PaginationData) -> PaginationOutput:
        '''Finds all foods which have a specific tag and returns a list of FoodBriefOutput.'''
        # Check if the tag exist
        try:
            tag = self.tag_repo.find_by_id(tag_id)

            # Find and return all foods in the tag
            foods = self.food_repo.find_all_by_tag_ordered_by_rating(tag.id)
            # Paginate favorite foods
            try:
                paginated_foods, pages = PaginatorUtil.paginate_query_set(foods, pagination_data)

                # Create pagination output
                data = list(map(self.food_brief_mapper.from_model, paginated_foods))

                # Create pagination output
                output = PaginatorUtil.create_pagination_output(data, pages, pagination_data.page)

                return output
            except:
                raise PageNotFoundException(detail= f'Page({pagination_data.page}) not found!')

        except Tag.DoesNotExist:
            raise TagNotFoundException(detail=f'Tag(id= {tag_id}) not found!')
    
    def find_favorite_foods(self, user_id: int, pagination_data: PaginationData) -> PaginationOutput:
        '''Finds the user favourite foods and returns a PaginationOutput.'''
        # Check if the user exist
        try:
            # Find and return all favorite foods
            favorite_foods = self.user_repo.get_favorite_foods(user_id)
            # Paginate favorite foods
            try:
                paginated_foods, pages = PaginatorUtil.paginate_query_set(favorite_foods, pagination_data)

                # Create pagination output
                data = list(map(self.food_brief_mapper.from_model, paginated_foods))

                # Create pagination output
                output = PaginatorUtil.create_pagination_output(data, pages, pagination_data.page)

                return output
            except:
                raise PageNotFoundException(detail= f'Page({pagination_data.page}) not found!')

        except User.DoesNotExist:
            raise UserNotFoundException(detail=f'User(id= {user_id}) not found!')

    def add_favorite_food(self, user_id: int, food_id: int) -> None:
        '''Adds a favorite food to user'''
        # Check if the user exist
        try:
            # Find and return all favorite foods
            user = self.user_repo.get_user_by_id(user_id)

            # Checking if the food exists
            try:
                food = self.food_repo.find_by_id(food_id)

                # Adding  a favorite food to user
                user.favorite_of.add(food)
                
                user.save()

            except Food.DoesNotExist:
                raise FoodNotFoundException(detail=f'Food(id={id}) not found!')

        except User.DoesNotExist:
            raise UserNotFoundException(detail=f'User(id= {user_id}) not found!')
