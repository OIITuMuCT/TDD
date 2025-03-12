from django.db import models

# Create your models here.

class User(models.Model):
    """ пользователь """
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'
    is_anonymous = False
    is_authenticated = True
    