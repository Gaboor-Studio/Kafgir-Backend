import attr

@attr.s
class AdminRegisterInput:
    '''This is a DTO for admin registeration. It is used in admin panel to create a new admin.'''

    username: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()
    email: str = attr.ib()
    password: str = attr.ib()
    password_repeat: str = attr.ib()
    is_superuser: bool = attr.ib()

@attr.s
class AdminUpdateProfileInput:
    '''This is a DTO for admin profile update. It does not take is_super_admin and password as parameters.'''

    username: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()
    email: str = attr.ib()
    is_superuser: bool = attr.ib()

@attr.s
class AdminSetPasswordInput:
    '''This is a DTO for setting admin's password. 
    We have this DTO since we have a different page for setting admin's password.'''
    
    new_password: str = attr.ib()
    new_password_repeat: str = attr.ib()

@attr.s
class AdminOutput:
    '''This is a DTO for showing admin details.'''

    id: int = attr.ib()
    username: str = attr.ib()
    email: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()
    is_superuser: bool = attr.ib()

@attr.s
class AdminBriefOutput:
    '''This is a DTO for showing a list of admins in admin panel.'''

    id: int = attr.ib()
    username: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()

