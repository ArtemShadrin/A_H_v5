import datetime

from rest_framework.exceptions import ValidationError

from amazing_hunting.settings import MIN_REGISTRATION_AGE, FORBIDDEN_MAIL_DOMAINS


def check_birth_date(value):
    today = datetime.date.today()
    age = (today.year - value.year - 1) + ((today.month, today.day) >= (value.month, value.day))
    if age < MIN_REGISTRATION_AGE:
        raise ValidationError(f"Ваш возраст {age} слишком мал для регистрации!")


def check_email(value):
    domain = value.split("@")[-1]
    if domain in FORBIDDEN_MAIL_DOMAINS:
        raise ValidationError(f"Регистрация с почтового домена {domain} запрещена!")
