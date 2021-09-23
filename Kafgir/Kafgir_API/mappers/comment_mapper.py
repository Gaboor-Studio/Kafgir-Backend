from ..models.comment import Comment
from ..dto.comment_dto import CommentOutput

class CommentMapper:
    ''' This is a mapper for converting comment default model to CommentOutput DTO'''

    def from_model(self, model: Comment) -> CommentOutput:
        '''Takes a model of comment and converts it to CommentOutput DTO'''

        if model == None:
            return None

        return CommentOutput(   id=model.pk,
                                user=model.user.pk,
                                date_time=model.date_time,
                                rating=model.rating,
                                text=model.text)