from rest_framework.exceptions import ValidationError


def check_not_true(value):
    if value:
        raise ValidationError("Значение не может быть True")