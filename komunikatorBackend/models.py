from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

class EmailUserManager(BaseUserManager):
    def create_user(self, email, password):
        if not email:
            raise ValueError('Email required')
        user = self.model(
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_admin = True
        user.save()
        return user

class EmailUser(AbstractBaseUser):
    email = models.EmailField(unique=True, db_index=True)
    USERNAME_FIELD = 'email'
    
    objects=EmailUserManager()


