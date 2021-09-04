import attr
import typing

@attr.s
class ProfileInput:
    username: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()

@attr.s 
class ProfileOutput:
    username: str = attr.ib()
    email: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()
    image: typing.Any=  attr.ib()

@attr.s
class ProfilePasswordChangeInput:
    old_password: str = attr.ib()
    new_password: str = attr.ib()
    new_password_rep: str = attr.ib()

@attr.s
class ProfileSetEmailInput: 
    email: str = attr.ib()

@attr.s
class ProfileSetPictureInput:
    image= attr.ib()



