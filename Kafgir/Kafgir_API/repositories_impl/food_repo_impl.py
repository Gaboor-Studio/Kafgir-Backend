from ..models.food import Food

from ..repositories.food_repo import FoodRepository

from typing import List

class FoodRepositoryImpl(FoodRepository):

    def find_by_id(self, id: int) -> Food:
        return Food.objects.get(pk=id)

    def save(self, food: Food) -> None:
        food.save()

    def delete_by_id(self, id: int) -> None:
        Food.objects.filter(pk=id).delete()

    def find_all(self) -> List[Food]:
        return list(Food.objects.all())