import attr

@attr.s
class UserRegisterInput:
    username: str = attr.ib()
    email: str = attr.ib()
    password: str = attr.ib()
    name: str = attr.ib(default=None)
    last_name: str = attr.ib(default=None)


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

@attr.s
class GetResetTokenInput:
    email: str = attr.ib()
    confirm_code: str = attr.ib()

@attr.s
class ResetPasswordInput:
    email: str = attr.ib()
    reset_token: str = attr.ib()
    new_password: str = attr.ib()
    new_password_rep: str = attr.ib()