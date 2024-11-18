from typing import Any
from django.http import HttpResponseForbidden
from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Event, Venue
from .forms import EventForm, VenueForm, EventUpdateForm
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from manage_accounts.permissions import CheckRolePermission

class EventOrganizerHome(TemplateView):
    template_name = 'event_organizer_home.html'


class CreateEventView(CheckRolePermission, CreateView):
    model = Event
    form_class = EventForm
    template_name = 'create_event.html'
    success_url = reverse_lazy('events_home')  

    def form_valid(self, form):
        # Set the organizer as the currently logged-in user
        form.instance.organizer = self.request.user
        form.save()
        messages.success(self.request, 'Event created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to create the event. Please correct the errors below.')
        return super().form_invalid(form)

class ManageEventsView(CheckRolePermission, TemplateView):
    template_name = 'event_mangement.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['events'] = Event.objects.all()
        return context
    
class UpdateEventView(CheckRolePermission , UpdateView):
    model = Event
    form_class = EventUpdateForm
    template_name = 'update_bookings.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Event updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update the Event. Please correct the errors below.')
        return super().form_invalid(form)

    def get_success_url(self):
        messages.success(self.request, "Event updated successfully!")
        return reverse_lazy('manage_events')  

def DeleteEventView(request, event_id):
    # Instantiate CheckRolePermission to check permissions
    # permission_check = CheckRolePermission()
    
   
    # if not permission_check.test_func():
    #     return HttpResponseForbidden("You do not have permission to delete users.")
    event = Event.objects.get(id=event_id)
    event.delete()
    return reverse_lazy('events_home')


class ManageAttendeesView(TemplateView):
    template_name = 'manage_attendees.html'

class AssignVenuesView(TemplateView):
    template_name = 'assign_venues.html'

class CreateVenueView(CheckRolePermission, CreateView):
    model = Venue
    form_class = VenueForm
    template_name = 'create_venue_manager.html'
    success_url = reverse_lazy('events_home')  

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Venue created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to create the venue. Please correct the errors below.')
        return super().form_invalid(form)

class ManageVenueView(CheckRolePermission ,TemplateView):
    template_name = 'manage_venue.html'

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["venue_details"] = Venue.objects.all()
        return context


