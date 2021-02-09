from djongo import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("User must have an Email Address")
        if not username:
            raise ValueError("User must Have a username")
        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(verbose_name="Username", max_length=30, null=False)
    email = models.EmailField(verbose_name="Email Address", max_length=30, unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'.Up to 15 digits "
                                         "allowed.")
    number = models.CharField(verbose_name="Phone Number", validators=[phone_regex], max_length=17)
    date_joined = models.DateTimeField(verbose_name="Join Date", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="Last Login Date", auto_now=True)
    password = models.CharField(verbose_name="Password", max_length=100, null=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    hide_email = models.BooleanField(default=True)

    objects = MyAccountManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

    def has_perms(self, perm_list, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_superuser
