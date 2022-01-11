from common.error import ValidatorException
from users.models import Person


def get_user_instance(username_or_id: str | int) -> Person:
    """returns user instance or exception on username or id"""
    if type(username_or_id) is str:
        username = username_or_id
        if Person.objects.filter(username=username).exists():
            return Person.objects.get(username=username)
        else:
            raise ValidatorException("User does not exist", "NoUser", 455)
    elif type(username_or_id) is int:
        pkid = username_or_id
        if Person.objects.filter(id=pkid).exists():
            return Person.objects.get(id=pkid)
        else:
            raise ValidatorException("User does not exist", "NoUser", 455)

