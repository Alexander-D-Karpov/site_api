from common.error import ValidatorException
from users.models import Person
from users.services.validate_password import validate_password


def change_password(user: Person, old_password: str, new_password: str) -> None:

    if not user.check_password(old_password):
        raise ValidatorException("Provided password is wrong", "WrongPas", 458)

    validate_password(new_password)

    user.set_password(new_password)
    user.save()
