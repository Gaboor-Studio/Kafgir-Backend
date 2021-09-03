import attr

@attr.s
class UserRegisterInput:
    username: str = attr.ib()
    email: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()
    password: str = attr.ib()

@attr.s
class PasswordResetTokenOutput:
    token: str = attr.ib()

@attr.s
class SendEmailInput:
    email: str = attr.ib()

@attr.s
class VerifyEmailInput:
    email: str = attr.ib()
    confirm_code: str = attr.ib()