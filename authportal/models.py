from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class StaffAndSuperuser(User):
    class Meta:
        proxy = True
        verbose_name = 'Staff/Superuser'
        verbose_name_plural = 'Staff/Superusers'