from django.db import models
from manage_accounts.models import User
# Create your models here.

class Venue(models.Model):
    name = models.CharField(max_length=255, verbose_name="Venue Name")
    location = models.CharField(max_length=500, verbose_name="Venue Location")
    capacity = models.PositiveIntegerField(verbose_name="Capacity")
    manager = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="managed_venues")

    def __str__(self):
        return self.name


class VenueAvailability(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="availabilities")
    date = models.DateField(verbose_name="Available Date")
    is_available = models.BooleanField(default=True, verbose_name="Is Available")

    def __str__(self):
        return f"{self.venue.name} - {self.date} ({'Available' if self.is_available else 'Unavailable'})"
    

class Booking(models.Model):
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name="bookings")
    event_name = models.CharField(max_length=255, verbose_name="Event Name")
    organizer = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Organizer")
    booking_date = models.DateField(verbose_name="Booking Date")
    attendees = models.PositiveIntegerField(verbose_name="Number of Attendees")

    def __str__(self):
        return f"Booking for {self.event_name} at {self.venue.name} on {self.booking_date}"
