import attr

@attr.s
class IngredientPieceOutput:
    id: int = attr.ib()
    name: str = attr.ib()
    amount: str = attr.ib()

@attr.s
class IngredientPieceInput:
    name: str = attr.ib()
    amount: str = attr.ib()
