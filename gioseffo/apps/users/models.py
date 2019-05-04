from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)
from django.db import models

from model_utils import Choices


class CustomUserManager(BaseUserManager):
    def create_user(self, username, full_name, password=None):
        """
        Creates and saves a User with the given username,
        full_name and password.
        """
        if not username:
            raise ValueError('Users must have a username')

        if not full_name:
            raise ValueError('Users must have a full name')

        user = self.model(username=username, full_name=full_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password):
        """
        Creates and saves a superuser with the given username,
        full_name and password.
        """
        user = self.create_user(username, full_name, password=password)

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(unique=True, max_length=255, db_index=True, null=True)
    full_name = models.CharField(max_length=255)
    birthday = models.DateField(null=True)
    email = models.CharField(unique=True, max_length=255, null=True, db_index=True)
    mobile_number = models.CharField(unique=True, max_length=255, null=True, db_index=True)
    GENDER = Choices(
        (0, 'blank', 'Prefer Not to Say'),
        (1, 'male', 'Male'),
        (2, 'female', 'Female')
    )
    gender = models.PositiveSmallIntegerField(choices=GENDER, default=GENDER.blank)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['full_name']

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.is_admin
