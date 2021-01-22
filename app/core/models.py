from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class UserManager(BaseUserManager):

    # read base user manager to understand normalize_email
    # used in below function or we can use of custom functions on
    # each filed including email to set normalization criteria such as
    # email should be in lowercase, correct format of email etc

    def create_user(self, email, password=None, **extra_fields):
        """Create and saves a new User"""
        if not email:
            raise ValueError('User must provide email address')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """Create and saves a new Super User"""
        if not email:
            raise ValueError('User must provide email address')
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """Custom user model that supports using email instead of username"""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()
    USERNAME_FIELD = 'email'
