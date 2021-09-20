import attr

@attr.s
class UserManagementCreateProfileInput:
    ''' This DTO puts constraints on usermanagement create user api input'''

    username: str = attr.ib()
    email: str = attr.ib()
    password: str = attr.ib()
    is_active: str = attr.ib()
    name: str = attr.ib(default=None)
    last_name: str = attr.ib(default=None)

@attr.s
class UserManagementEditProfileInput:
    ''' This DTO puts constraints on usermanagement edit user api input'''

    username: str = attr.ib(default=None)
    name: str = attr.ib(default=None)
    last_name: str = attr.ib(default=None)
    is_active: str = attr.ib(default=None)

@attr.s
class UserManagementSetPasswordInput:
    ''' This DTO puts constraints on usermanagement change password api input'''

    new_password: str = attr.ib()

@attr.s
class UserManagementSetPfpInput:
    ''' This DTO puts constraints on usermanagement set profile picture api input'''

    image= attr.ib()


@attr.s
class UserManagementProfileOutput:
    ''' This DTO considers the shape of outputting the users in usermanagement api'''

    id: int = attr.ib()
    username: str = attr.ib()
    email: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()
    image= attr.ib()
    is_active: bool = attr.ib()