from ..repositories.tag_repo import TagRepository

from ..models.tag import Tag
from ..models.food import Food

from typing import List

class TagRepositoryImpl(TagRepository):

    def find_by_id(self, id: int) -> Tag:
        return Tag.objects.get(pk=id)

    def find_all(self) -> List[Tag]:
        return list(Tag.objects.all())

    def save(self, tag: Tag) -> None:
        tag.save()

    def delete_by_id(self, id: int) -> None:
        Tag.objects.filter(id=id).delete()

    def find_main_tag(self) -> List[Tag]:
        return list(Tag.objects.filter(is_main=True).order_by('display_order'))

    def find_primary_tag(self) -> List[Tag]:
        return list(Tag.objects.filter(is_primary=True).order_by('display_order'))

    def get_some_food_by_tag_id(self, id: int, num: int) -> List[Food]:
        foods = Tag.objects.get(pk=id).food
        food_count = foods.count()
        if(food_count>=num) :
            return list(foods.order_by('rating')[-1*num:])
        return list(foods.all().order_by('-rating'))
