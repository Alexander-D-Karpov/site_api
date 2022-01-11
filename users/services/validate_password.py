from common.error import ValidatorException
from users.services.validators import RegexValidator, ValidatorChain


def validate_password(password: str) -> None:
    num_validator = RegexValidator(
        "\d",
        ValidatorException(
            "The password must contain at least 1 number", "NumPas", 452
        ),
    )
    uppercase_validator = RegexValidator(
        "[A-Z]",
        ValidatorException(
            "The password must contain at least 1 UPPERCASE symbol", "UpPas", 453
        ),
    )
    special_character_validator = RegexValidator(
        "[()[\]{}|\\`~!@#$%^&*_\-+=;:'\",<>./?]",
        ValidatorException(
            "The password must contain at least 1 special character: "
            + """()[]{}|\`~!@#$%^&*_-+=;:'\",<>./?""",
            "SpecPas",
            454,
        ),
    )

    chain = ValidatorChain(
        [num_validator, uppercase_validator, special_character_validator]
    )

    chain.check(password)
