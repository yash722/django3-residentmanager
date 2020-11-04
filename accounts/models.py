from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, society_name, password=None):
        if not society_name:
            raise ValueError('You must give name of a society')
        user = self.model(society_name=society_name)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, society_name , password):
        user = self.create_user(
                society_name=society_name,
                password=password)
        user.is_staff = True
        user.is_admin = True
        user.save(using=self._db)
        return user

    def create_staffuser(self, society_name ,password):
        user = self.create_user(
            society_name=society_name,
            password=password,
        )
        user.is_staff = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    society_name = models.CharField(max_length=255, unique=True, verbose_name="Enter name of society",default="")
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'society_name'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


def __str__(self):
    return self.society_name
