from __future__ import annotations

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, UserManager

from model_utils.models import TimeStampedModel

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


class CustomUserManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):

        # Assuming the username field is 'username'
        if not username:
            raise ValueError("The given username must be set")

        user = self.model.objects.filter(email=email).first()
        if user:
            return user

        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            **extra_fields,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser, TimeStampedModel):
    objects = CustomUserManager()

    email = models.EmailField(_("email address"), blank=True, null=True, unique=True)

    def __str__(self) -> str:
        full_name = self.get_full_name()
        return full_name if full_name else self.username

    def get_jwt_tokens(self):
        token = (
            OutstandingToken.objects.filter(user=self, expires_at__gt=timezone.now(), blacklistedtoken__isnull=True)
            .order_by("-created_at")
            .first()
        )

        refresh = RefreshToken.for_user(self) if not token else RefreshToken(token.token)

        return {"refresh": str(refresh), "access": str(refresh.access_token)}