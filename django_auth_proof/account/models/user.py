from django.contrib.auth.models import AbstractUser
from django.db import models



class User(AbstractUser):
    profiles_choice = (('T', 'Teatcher'), ('S', 'Student'))
    profile = models.CharField(max_length=1, choices=profiles_choice)

    @property
    def profile_display(self):
        return self.get_profile_display()