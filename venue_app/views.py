from django.shortcuts import redirect
from django.views.generic.edit import UpdateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Venue, VenueAvailability, Booking
from .forms import VenueUpdateForm, VenueAvailabilityForm, BookingForm
from django.views.generic import TemplateView


class VenueHome(TemplateView):
    template_name = 'venue_home.html'

class VenueUpdateView(UpdateView):
    model = Venue
    form_class = VenueUpdateForm
    template_name = 'update_venue.html'
    success_url = reverse_lazy('manage_venue')  

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Venue updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update the venue. Please correct the errors below.')
        return super().form_invalid(form)

def VenueDeleteView(request, venue_id):
    venue = Venue.objects.get(id=venue_id)
    venue.delete()
    messages.success(request, 'Venue deleted successfully!')
    return reverse_lazy('manage_venue')  


class ManageAvailabilityView(FormView):
    template_name = 'manage_availability.html'
    form_class = VenueAvailabilityForm
    success_url = reverse_lazy('venue_home')

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'VenueAvailability created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to create the VenueAvailability. Please correct the errors below.')
        return super().form_invalid(form)
    
class UpdateAvailabilityView(UpdateView):
    model = VenueAvailability
    form_class = VenueAvailabilityForm
    template_name = 'update_availability.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Availability updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to update the Availability. Please correct the errors below.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('manage_venue') 

def AvailabilityDeleteView(request, availability_id):
    availability = VenueAvailability.objects.get(id=availability_id)
    availability.delete()
    messages.success(request, 'Availability deleted successfully!')
    return redirect(reverse_lazy('manage_venue'))  

class ManageBookingsView(FormView):
    form_class = BookingForm
    template_name = 'manage_bookings.html'
    success_url = reverse_lazy('venue_home')  

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Booking created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'Failed to create the Booking. Please correct the errors below.')
        return super().form_invalid(form)  
    
class UpdateBookingView(UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'update_booking.html'

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Booking updated successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        
        messages.error(self.request, 'Failed to update the Booking. Please correct the errors below.')
        return super().form_invalid(form)

    def get_success_url(self):
        return reverse_lazy('manage_venue') 
    
def DeleteBookingView(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.delete()
    messages.success(request, 'Booking deleted successfully!')
    return redirect(reverse_lazy('manage_venue'))

class VenueMoreDetails(TemplateView):
    template_name = 'venue_more_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        venue_id = self.kwargs['venue_id']
        venue = Venue.objects.get(id=venue_id)
        context['venue'] = venue
        context['venue_bookings'] = Booking.objects.filter(venue=venue)
        context['venue_availability'] = VenueAvailability.objects.filter(venue=venue)
        return context