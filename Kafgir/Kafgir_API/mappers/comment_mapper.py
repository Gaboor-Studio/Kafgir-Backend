from ..models.comment import Comment
from ..dto.comment_dto import CommentOutput,MyCommentOutput,CommentBriefOutput

class CommentMapper:
    ''' This is a mapper for converting comment default model to CommentOutput DTO'''

    def from_model(self, model: Comment) -> CommentOutput:
        '''Takes a model of comment and converts it to CommentOutput DTO'''

        if model == None:
            return None

        return CommentOutput(   id=model.pk,
                                user_id=model.user.pk,
                                username=model.user.username,
                                user_pic=model.user.get_image(),
                                date_time=model.date_time,
                                rating=model.rating,
                                text=model.text)

class CommentBriefMapper:
    ''' This is a mapper for converting comment default model to CommentBriefOutput DTO'''

    def from_model(self, model: Comment) -> CommentBriefOutput:
        '''Takes a model of comment and converts it to CommentBriefOutput DTO'''

        if model == None:
            return None

        return CommentBriefOutput(   id=model.pk,
                                user_id=model.user.pk,
                                username=model.user.username,
                                date_time=model.date_time,
                                rating=model.rating,
                                text=model.text)

class MyCommentMapper:
    ''' This is a mapper for converting comment default model to MyCommentOutput DTO'''

    def from_model(self, model: Comment) -> MyCommentOutput:
        '''Takes a model of comment and converts it to MyCommentOutput DTO'''

        if model == None:
            return None

        return MyCommentOutput(   id=model.pk,
                                user_id=model.user.pk,
                                username=model.user.username,
                                user_pic=model.user.get_image(),
                                date_time=model.date_time,
                                rating=model.rating,
                                text=model.text,
                                confirmed=model.confirmed)