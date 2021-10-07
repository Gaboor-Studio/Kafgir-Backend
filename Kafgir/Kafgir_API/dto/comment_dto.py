import attr
from datetime import datetime

from typing import List

@attr.s
class CommentOutput:
    '''This is a DTO for showing comment details.'''
    id: int = attr.ib()
    user_id: int = attr.ib()
    username: str = attr.ib()
    user_pic: str = attr.ib()
    date_time: datetime = attr.ib()
    rating: int = attr.ib()
    text: str = attr.ib()

@attr.s
class CommentBriefOutput:
    '''This is a DTO for showing comments in admin panel list.'''
    id: int = attr.ib()
    user_id: int = attr.ib()
    username: str = attr.ib()
    date_time: datetime = attr.ib()
    rating: int = attr.ib()
    text: str = attr.ib()

@attr.s
class MyCommentOutput:
    '''This is a DTO for showing my comment.'''
    id: int = attr.ib()
    user_id: int = attr.ib()
    username: str = attr.ib()
    user_pic: str = attr.ib()
    date_time: datetime = attr.ib()
    rating: int = attr.ib()
    text: str = attr.ib()
    confirmed: bool = attr.ib()

@attr.s
class CommentInput:
    '''This is a DTO for creating comment .'''
    rating: int = attr.ib()
    text: str = attr.ib()

@attr.s
class CommentIdListInput:
    '''This is a DTO for administrators to confirm user comments.'''
    commentid_list: List[int] = attr.ib()