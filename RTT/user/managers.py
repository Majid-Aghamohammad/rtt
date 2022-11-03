
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.hashers import make_password


class UserManager(BaseUserManager):

    use_in_migrations = True

    # def validate_password(self, value: str):
    #     return make_password(value)

    def _create_user(self, username, email, password, **extra_fields):
        """Create and save a User with the given username and password."""
        if email:
            email = self.normalize_email(email)
        user = self.model(
            username=username, email=email , **extra_fields
        )
        if password:
            user.set_password(password)
        else:
            user.set_unusable_password()
        user.save(using=self._db)
        return user


    def create_user(self, username, email, password, **extra_fields):
        """Create and save a regular User with the given email/phone and password."""
        if not email:
            raise ValueError("email must be set")
        user=self.model(email=self.normalize_email(email))
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user = self._create_user(
            username=username,
            email=email,
            password=password,
        )
        return user
    def create_staffuser(self, username, email, password, **extra_fields):
        """
        Creates and saves a staff user with the given username and password.
        """
        extra_fields.setdefault("is_superuser", False)
        user = self._create_user(
            username=username,
            email=email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password=None,**extra_fields):
        """Create and save a super user."""
        user = self._create_user(
        email = email,
        username = username,
        password= password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user