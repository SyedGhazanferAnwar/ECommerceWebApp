from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, firstName, lastName, address, password, active, staff, admin):
        if not email:
            raise ValueError("Users must have a valid Email address")
        if not staff and not admin:
            if not firstName:
                raise ValueError("Users must have a valid First Name")
            if not lastName:
                raise ValueError("Users must have a valid Last Name")
            if not address:
                raise ValueError("Users must have a valid address")
        user = self.model(
            email=email
        )
        user.firstName = firstName
        user.lastName = lastName
        user.address = address
        user.staff = staff
        user.active = active
        user.admin = admin
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_staffuser(self, email, password=None, firstName="", lastName="", *args, **kwargs):
        if not password:
            raise ValueError("User nust have a valid password.")
        user = self.create_user(
            email,
            firstName,
            firstName,
            "address",
            password,
            True,
            True,
            True,
        )
        return user

    def create_superuser(self, email, firstName="", password=None, lastName="", *args, **kwargs):
        if not password:
            raise ValueError("User nust have a valid password.")
        user = self.create_user(
            email,
            firstName,
            lastName,
            "addressssssssss",
            password,
            True,
            True,
            True
        )
        return user


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    firstName = models.CharField(max_length=255)
    lastName = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.firstName + self.lastName

    def get_short_name(self):
        return self.firstName

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
