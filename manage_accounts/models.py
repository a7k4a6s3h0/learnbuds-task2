from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    ROLE_CHOICES = [
        ('organizer', 'Event Organizer'),
        ('attendee', 'Attendee'),
        ('venue_manager', 'Venue Manager'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='attendee')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
