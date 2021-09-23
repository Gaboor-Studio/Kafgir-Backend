import attr
from datetime import datetime

from typing import List

@attr.s
class CommentOutput:
    '''This is a DTO for showing comment details.'''

    id: int = attr.ib()
    user: int = attr.ib()
    date_time: datetime = attr.ib()
    rating: int = attr.ib()
    text: str = attr.ib()

@attr.s
class CommentInput:
    '''This is a DTO for creating comment .'''

    rating: int = attr.ib()
    food: int = attr.ib()
    text: str = attr.ib()

@attr.s
class CommentBriefInput:
    '''This is a DTO for updating comment . It does not take food id as parameters.'''

    rating: int = attr.ib()
    text: str = attr.ib()

@attr.s
class CommentIdListInput:
    '''This is a DTO for administrators to confirm user comments.'''
    commentid_list: List[int] = attr.ib()