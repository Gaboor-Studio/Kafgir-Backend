import attr


@attr.s
class RecipeItemOutput:
    id: int = attr.ib()
    step: int = attr.ib()
    text: str = attr.ib()

@attr.s
class RecipeItemInput:
    step: int = attr.ib()
    text: str = attr.ib()
