from typing import List

from ...dto.food_dto import FoodOutput
from ...dto.comment_dto import CommentOutput,CommentInput,CommentBriefInput

from ...dto.food_dto import FoodOutput, FoodBriefOutput
from ...usecases.member.member_food_usecase import MemberFoodUsecase
from ...models.food import Food
from ...models.comment import Comment
from ...models.user import User
from ...models.shopping_list_item import ShoppingListItem
from ...models.tag import Tag
from ...exceptions.not_found import FoodNotFoundException,TagNotFoundException
from ...repositories.food_repo import FoodRepository
from ...repositories.tag_repo import TagRepository
from ...repositories.shopping_list_repo import ShoppingListRepository
from ...repositories.user_repo import UserRepository
from ...repositories.comment_repo import CommentRepository
from ...mappers.food_mappers import FoodMapper
from ...mappers.comment_mapper import CommentMapper
from ...exceptions.not_found import CommentNotFoundException,FoodNotFoundException
from ...mappers.food_mappers import FoodMapper,FoodBriefMapper

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
                       food_brief_mapper: FoodBriefMapper = Provide['food_brief_mapper']):
        '''Constructor with 8 arguments which are dependencies of this service. They are automatically injected by the framework'''
        self.tag_repo = tag_repo
        self.food_repo = food_repo
        self.food_mapper = food_mapper
        self.food_brief_mapper = food_brief_mapper
        self.shopping_list_repo = shopping_list_repo
        self.comment_repo = comment_repo
        self.user_repo = user_repo
        self.comment_mapper = comment_mapper

    def find_by_id(self, user_id: int, food_id: int) -> FoodOutput:
        '''Finds a food given its id and returns a FoodOutput DTO.'''
        #Checking if the food exists
        try:
            food = self.food_repo.find_by_id(food_id)
            food_output = self.food_mapper.from_model(food)

            # Checking if we have a current logged in user
            if not user_id==None:
                # Finding user comments on the food
                my_comment = self.find_comment_by_user_id(food_id=food_id,id=user_id)
                if not my_comment==None:
                    food_output.my_comment = my_comment
            
            food_output.comments = list(map(self.comment_mapper.from_model, self.comment_repo.get_some_food_comments(num=6, food=food)))
            return food_output
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

    def get_some_food_comments(self, food_id: int, num: int) -> List[CommentOutput]:
        '''Gets a number of food comments and returns a list of CommentOutput DTO.'''
        # Checking if the food exists
        try:
            food = self.food_repo.find_by_id(food_id)

            # Converting the food comments to a list of CommentOutput and returning them 
            return list(map(self.comment_mappeXr.from_model, self.comment_repo.get_some_food_comments(num=num, food=food)))
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={food_id}) not found!')

    def get_food_comments(self, food_id: int) -> List[CommentOutput]:
        '''Gets all comments of the food given its id and returns a list of CommentOutput DTO.'''
        # Checking if the food exists
        try:
            food = self.food_repo.find_by_id(food_id)

            # Converting the food comments to a list of CommentOutput and returning them 
            return list(map(self.comment_mapper.from_model, self.comment_repo.get_food_comments(food=food)))
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={food_id}) not found!') 

    def find_comment_by_user_id(self, id: int, food_id: int) -> CommentOutput:
        '''Finds the user comment on the post if exists.'''
        try:
            food = self.food_repo.find_by_id(food_id)
            #TODO: remove the if. user try except
            if self.comment_repo.are_there_any_user_comment(id=id, food=food):
                return self.comment_mapper.from_model(self.comment_repo.find_comment_by_user_id(food=food, id=id))
            return None
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={food_id}) not found!')

    def add_comment(self, food_id: int, input:  CommentInput, user: User) -> None:
        '''Posts a comment on the food with the given user.'''
        try:
            food = self.food_repo.find_by_id(food_id)
            if not self.comment_repo.are_there_any_user_comment(id=user.pk, food=food_id):
                comment = Comment(food=food,user=user,confirmed=False,text=input.text,rating=input.rating)
                comment.save()
            #TODO: else throw an error
        except Food.DoesNotExist:
            raise FoodNotFoundException(detail=f'Food(id={food_id}) not found!')

    def find_all_with_tag(self, tag_id: int) -> List[FoodBriefOutput]:
        '''Finds all foods which have a specific tag and returns a list of FoodBriefOutput.'''
        # Check if the tah exist
        try:
            tag = self.tag_repo.find_by_id(tag_id)

            # Find and return all foods in the tag
            foods = self.food_repo.find_all_by_tag_ordered_by_rating(tag.id)
            return list(map(self.food_brief_mapper.from_model, foods))
        except Tag.DoesNotExist:
            raise TagNotFoundException(detail=f'Tag(id= {tag_id}) not found!')
    
