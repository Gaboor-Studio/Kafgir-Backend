import attr
from datetime import datetime

@attr.s
class CommentOutput:
    id: int = attr.ib()
    user: int = attr.ib()
    date_time: datetime = attr.ib()
    rating: int = attr.ib()
    text: str = attr.ib()

@attr.s
class CommentInput:
    rating: int = attr.ib()
    food: int = attr.ib()
    text: str = attr.ib()

@attr.s
class CommentBriefInput:
    rating: int = attr.ib()
    text: str = attr.ib()
