import attr

@attr.s
class IngredientOutput:
    id: int = attr.ib()
    name: str = attr.ib()

@attr.s
class IngredientInput:
    name: str = attr.ib()
