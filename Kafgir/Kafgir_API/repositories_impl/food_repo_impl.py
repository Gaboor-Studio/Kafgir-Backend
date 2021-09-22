from ..models.food import Food
from ..models.tag import Tag

from django.db.models import QuerySet

from ..repositories.food_repo import FoodRepository

class FoodRepositoryImpl(FoodRepository):

    def find_by_id(self, id: int) -> Food:
        return Food.objects.get(pk=id)

    def save(self, food: Food) -> None:
        food.save()

    def delete_by_id(self, id: int) -> None:
        Food.objects.filter(pk=id).delete()

    def find_all(self) -> QuerySet:
        return Food.objects.all()

    def find_all_by_tag_ordered_by_rating(self, tag_id: int) -> QuerySet:
        return Food.objects.filter(tags__id=tag_id).order_by('-rating')