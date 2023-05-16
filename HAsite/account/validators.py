from django.core.exceptions import ValidationError


def length_validator(value):
    if len(value) < 8:
        raise ValidationError("min length is 8")
    if len(value) > 8:
        raise ValidationError("max length is 32")
