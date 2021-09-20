from ..models.comment import Comment
from ..dto.comment_dto import CommentOutput

class CommentMapper:

    def from_model(self, model: Comment) -> CommentOutput:
        if model == None:
            return None

        return CommentOutput(   id=model.pk,
                                user=model.user.pk,
                                date_time=model.date_time,
                                rating=model.rating,
                                text=model.text)