from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    COMMON = 1
    ADVANCE = 2
    TYPES = [
        (COMMON, 'common'),
        (ADVANCE, 'advance')
    ]
    type = models.PositiveSmallIntegerField(default=COMMON, choices=TYPES)
