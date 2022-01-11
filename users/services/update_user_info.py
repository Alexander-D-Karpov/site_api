from users.models import Person
from users.services.get_and_authenticate_user import get_and_authenticate_user


def update_user_info(
    user: Person,
    **extra_fields) -> Person:
    n_user = Person(id=user.id, **extra_fields)
    n_user.save()
    return n_user
