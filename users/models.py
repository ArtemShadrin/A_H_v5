import datetime

from django.contrib.auth.models import AbstractUser
from django.db import models

from users.validators import check_birth_date, check_email


class Location(models.Model):
    name = models.CharField(max_length=200, unique=True)
    lat = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)
    lng = models.DecimalField(max_digits=8, decimal_places=6, null=True, blank=True)

    class Meta:
        verbose_name = "Местоположение"
        verbose_name_plural = "Местоположения"

    def __str__(self):
        return self.name


class UserRoles(models.TextChoices):
    MEMBER = 'member', "Пользователь"
    MODERATOR = 'moderator', "Модератор"
    ADMIN = 'admin', "Админ"


class User(AbstractUser):
    role = models.CharField(max_length=10, choices=UserRoles.choices, default=UserRoles.MEMBER)
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    locations = models.ManyToManyField(Location)
    birth_date = models.DateField(validators=[check_birth_date])
    email = models.EmailField(validators=[check_email], unique=True)

    def save(self, *args, **kwargs):
        self.set_password(raw_password=self.password)
        today = datetime.date.today()
        if self.birth_date:
            self.age = (today.year - self.birth_date.year - 1) + (
                    (today.month, today.day) >= (self.birth_date.month, self.birth_date.day))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.username
