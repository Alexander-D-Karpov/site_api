import pytest

from users.services.create_user import create_user
from users.services.get_user_instance import get_user_instance


def test_user_create():
    create_user("dufghoiug", "dioufghogrh@odig.oiderhg", "sgijehgsiu@203", "sgijehgsiu@203")
    assert get_user_instance("dufghoiug").username == "dufghoiug"
