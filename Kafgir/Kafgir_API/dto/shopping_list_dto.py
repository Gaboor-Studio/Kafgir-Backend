import attr

@attr.s
class ShoppingListItemOutput:
    id: int = attr.ib()
    title: str = attr.ib()
    done: bool = attr.ib()
    amount: int = attr.ib()
    unit: str = attr.ib()

@attr.s
class ShoppingListItemInput:
    title: str = attr.ib()
    done: bool = attr.ib()
    amount: int = attr.ib()
    unit: str = attr.ib()

@attr.s
class ShoppingListItemBriefInput:
    title: str = attr.ib()
    amount: int = attr.ib()
    unit: str = attr.ib()