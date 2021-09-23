from django.db.models import QuerySet

from ..models.food import Food
from ..models.tag import Tag
from ..repositories.food_repo import FoodRepository

class FoodRepositoryImpl(FoodRepository):
    '''This is an implemetation of the FoodRepository.'''

    def find_by_id(self, id: int) -> Food:
        '''Finds a food given its id. It raises Food.DoesNotExist exception if the food does not exist.'''
        return Food.objects.get(pk=id)

    def save(self, food: Food) -> None:
        '''Saves or updates the given food in database.'''
        food.save()

    def delete_by_id(self, id: int) -> None:
        '''Deletes a food given its id.'''
        Food.objects.filter(pk=id).delete()

    def find_all(self) -> QuerySet:
        '''Finds all foods and returns a QuerySet of them.'''
        return Food.objects.all()

    def find_all_by_tag_ordered_by_rating(self, tag_id: int) -> QuerySet:
        '''Finds all food in a specific tag given the tag id and orders them by food rating and returns a QuerySet.'''
        return Food.objects.filter(tags__id=tag_id).order_by('-rating')