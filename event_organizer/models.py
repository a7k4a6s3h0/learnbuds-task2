from django.db import models
from manage_accounts.models import User
from venue_app.models import Venue

# Create your models here.

class Event(models.Model):

    OPTIONS = [
        ('active', 'Active'),
        ('upcoming', 'Upcoming')
    ]

    name = models.CharField(max_length=255, verbose_name="Event Name")
    description = models.TextField(verbose_name="Event Description")
    date = models.DateField(verbose_name="Event Date")
    time = models.TimeField(verbose_name="Event Time")
    status = models.CharField(choices=OPTIONS, max_length=50, default='upcoming')
    venue = models.ForeignKey(Venue, on_delete=models.SET_NULL, null=True, related_name="events")
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="organized_events")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    def __str__(self):
        return self.name
