from django.db import models
from event_organizer.models import Event
from manage_accounts.models import User
# Create your models here.
class Attendee(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="attendees")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="event_attendances")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration Date")

    def __str__(self):
        return f"{self.user.username} - {self.event.name}"
    
class Registration(models.Model):
    STATUS_CHOICES = [
        ('registered', 'Registered'),
        ('canceled', 'Canceled'),
    ]
    
    attendee = models.ForeignKey(User, on_delete=models.CASCADE, related_name="registrations")
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="registrations")
    registration_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration Date")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='registered')

    def __str__(self):
        return f"{self.attendee.username} - {self.event.name}"

