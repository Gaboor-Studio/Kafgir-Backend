from django.test import TestCase

from .models.food import Food
from .usecases.member.member_food_usecase import MemberFoodUsecase

from dependency_injector.wiring import inject,Provide

# Create your tests here.
class MemberFoodUsecaseTest(TestCase):

    @inject
    def __init__(self, methodName: str = ..., member_food_usecase: MemberFoodUsecase = Provide['member_food_usecase']) -> None:
        super().__init__(methodName=methodName)
        self.member_food_usecase = member_food_usecase

    def setUp(self) -> None:
        food = Food(title='Gheyme', level=2, cooking_time='1 hour')
        food.save()

    @inject
    def test_find_by_id(self):
        food = self.member_food_usecase.find_by_id(None, 1)
        self.assertEqual(food.title, 'Gheyme', "Must be Gheyme")