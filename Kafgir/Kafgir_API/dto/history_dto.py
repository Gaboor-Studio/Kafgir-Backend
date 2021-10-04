from typing import List
import attr
from ..dto.tag_dto import PrimaryTagOutput

@attr.s
class HistoryInput:
    ''' It's a DTO to collect search history for a user! '''
    title: str = attr.ib()
    category: int = attr.ib(default=None)
    level: int = attr.ib(default=None)
    cooking_time: str = attr.ib(default=None)
    ingredients: str = attr.ib(default=None)

@attr.s
class HistoryOutput:
    ''' It's a DTO to output a single user's search history! '''
    id: int = attr.ib()
    title: str = attr.ib()
    category: PrimaryTagOutput = attr.ib()
    level: int = attr.ib()
    cooking_time: str = attr.ib()
    ingredients: List[str] = attr.ib()
    time: str = attr.ib()