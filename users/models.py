from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from django.db import models


class CustomUserModel(BaseUserManager):
    def create_user(self, username, password, is_active=True,
                    is_staff=False, is_superuser=False, **extra_fields):
        user = self.model(
            username=username,
            is_active=is_active,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        return self.create_user(username=username, password=password, is_superuser=True, is_active=True, is_staff=True,
                                **extra_fields)


class UserModel(PermissionsMixin, AbstractBaseUser):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=128)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)

    objects = CustomUserModel()

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
