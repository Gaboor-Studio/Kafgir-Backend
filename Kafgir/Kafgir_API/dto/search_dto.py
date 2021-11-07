import attr

@attr.s
class SearchInput:
    ''' This DTO class represents the group of attributes we need for search API '''

    title : str = attr.ib(default=None)
    category : int = attr.ib(default=None)
    ingredients : str = attr.ib(default=None)
    level : int = attr.ib(default=None)
    lct : str = attr.ib(default=None)
    uct : str = attr.ib(default=None)