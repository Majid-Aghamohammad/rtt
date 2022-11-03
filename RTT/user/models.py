from django.db import models
from django.contrib.auth.models import (AbstractBaseUser,PermissionsMixin) 
from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from .managers import UserManager
# Create your models here.





class User(AbstractBaseUser,PermissionsMixin):
    """User Models Fields"""
    username = models.CharField(max_length=500, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    password = models.CharField(max_length=128)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    ## define the user manager class for User
    objects = UserManager()
    # necessary to use the django authentication framework: this field is used as username

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    def __str__(self):
        """User str representation"""
        return f"{self.username}"

    # @property
    # def is_admin_user(self):
    #     """User Admin or staff"""
    #     return self.is_staff or self.is_superuser

