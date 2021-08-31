import attr

@attr.s
class UserRegisterInput:
    username: str = attr.ib()
    email: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()
    password: str = attr.ib()
