import attr
import typing

@attr.s
class ProfileInput:
    ''' This DTO is used in profile related usecases to get input from user'''
    name: str = attr.ib()
    last_name: str = attr.ib()

@attr.s 
class ProfileOutput:
    ''' This DTO is used in profile related usecases to output details about users'''
    username: str = attr.ib()
    email: str = attr.ib()
    name: str = attr.ib()
    last_name: str = attr.ib()
    image: typing.Any=  attr.ib()

@attr.s
class ProfilePasswordChangeInput:
    ''' This DTO is used in profile related usecases to gather information needed for changin user's password'''
    old_password: str = attr.ib()
    new_password: str = attr.ib()
    new_password_rep: str = attr.ib()

@attr.s
class ProfileSetEmailInput: 
    ''' This DTO is used in profile related usecases only to get new email from user '''
    email: str = attr.ib()

@attr.s
class ProfileSetPictureInput:
    ''' This DTO is used in profile related usecases only to get new picture from input to be set as user profile picture'''
    image= attr.ib()



