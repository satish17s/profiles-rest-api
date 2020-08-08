from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserProfileManager(BaseUserManager):
    """manager for user profile"""

    def create_user(self,email,name,password=None):
        """create a new User profile"""
        if not email:
            raise ValueError('user must have an email address')

        email=self.normalize_email(email)
        user=self.model(email=email,name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """create profile for superuser"""
        user=self.create_user(email,name,password)

        user.is_superuser=True
        user.is_staff=True
        user.save(using=self.db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """database for user in system"""
    email=models.EmailField(max_length=255,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)

    objects=UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']


    def get_full_name(self):
        """helps to retrive full name of user"""
        return self.name

    def get_short_name(self):
        """helps to retrive short name of user"""
        return self.name

    def __str__(self):
        """gives sting representation of userprofile class"""
        return self.email
