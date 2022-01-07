from users.error import ValidatorException
from users.models import Person


def get_user_instance(username: str) -> Person:
    """returns user instance or exception on username"""

    if Person.objects.filter(username=username).exists():
        return Person.objects.get(username=username)
    else:
        raise ValidatorException("User does not exist", "NoUser", 455)
