from common.error import ValidatorException
from users.models import Person


def delete_user(username: str) -> None:
    """returns user instance or exception on username"""

    if Person.objects.filter(username=username).exists():
        Person.objects.get(username=username).delete()
    else:
        raise ValidatorException("User does not exist", "NoUser", 455)
