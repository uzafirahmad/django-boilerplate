from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import PermissionsMixin


# Create your models here.
class MyUserManager(BaseUserManager):

    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")
        user= self.model(
            email=self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(verbose_name="email",max_length=60,unique=True)
    username=models.CharField(max_length=30, unique=True)
    date_joined=models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    password=models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects = MyUserManager() 

    USERNAME_FIELD= 'email'
    REQUIRED_FIELDS = ['username']