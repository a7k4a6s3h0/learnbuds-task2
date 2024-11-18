from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import View
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Event, Registration
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import FormView
from .forms import RegistrationForm, UpdateRegistrationForm, UpdateProfileForm
from manage_accounts.permissions import CheckRolePermission


class AttendeeHomePageView(TemplateView):
    template_name = "attendee_home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['upcoming_events'] = Event.objects.filter(status='upcoming').order_by('date')
        context['my_registrations'] = Registration.objects.filter(attendee=user).select_related('event')
        return context

class RegisterEventView(CheckRolePermission, View):
    template_name = 'register_event.html'

    def get(self, request, *args, **kwargs):
        # Retrieve the event
        event = get_object_or_404(Event, id=self.kwargs.get('event_id'))
        form = RegistrationForm()
        return render(request, self.template_name, {'form': form, 'event': event})

    def post(self, request, *args, **kwargs):
        # Retrieve the event
        event = get_object_or_404(Event, id=self.kwargs.get('event_id'))

        # Check if the user is already registered
        if Registration.objects.filter(attendee=request.user, event=event).exists():
            messages.warning(request, 'You are already registered for this event.')
            return redirect('attendee_home')

        # Create the registration for the user and the event
        Registration.objects.create(attendee=request.user, event=event)
        messages.success(request, 'You have successfully registered for the event.')
        return redirect('attendee_home')



class UpdateRegistrationView(CheckRolePermission, FormView):
    form_class = UpdateRegistrationForm
    template_name = 'update_registration.html'

    def get_success_url(self):
        # Redirect to the attendee home page after successfully updating the registration
        return reverse('attendee_home')  # Use reverse instead of redirect here

    def get_object(self):
        # Fetch the registration object that needs to be updated
        registration_id = self.kwargs['registration_id']
        return get_object_or_404(Registration, id=registration_id)

    def get_initial(self):
        # Pre-populate the form with the current registration status
        registration = self.get_object()
        return {'status': registration.status}

    def form_valid(self, form):
        # Update the registration with the new status
        registration = self.get_object()
        registration.status = form.cleaned_data['status']
        registration.save()
        messages.success(self.request, 'Your registration status has been updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # If form is invalid, return with an error message
        messages.error(self.request, 'There was an error updating your registration.')
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        # Add the registration object to the context
        context = super().get_context_data(**kwargs)
        context['registration'] = self.get_object()
        return context


class DeleteRegistrationView(CheckRolePermission, View):
    def post(self, request, event_id, *args, **kwargs):
        # Get the event and the registration for the logged-in user
        event = get_object_or_404(Event, id=event_id)
        registration = get_object_or_404(Registration, attendee=request.user, event=event)

        # Delete the registration
        registration.delete()
        messages.success(request, 'Your registration for the event has been successfully deleted.')

        return redirect('attendee_home')  # Redirect to the attendee's home/dashboard page
    

class UpdateProfileView(CheckRolePermission, FormView):
    form_class = UpdateProfileForm
    template_name = 'update_profile.html'
    
    def get_success_url(self):
        # After a successful update, redirect to the attendee home page or profile page
        return reverse_lazy('attendee_home')

    def get_initial(self):
        # Pre-populate the form with the current user's data
        return {
            'first_name': self.request.user.first_name,
            'last_name': self.request.user.last_name,
            'email': self.request.user.email
        }

    def form_valid(self, form):
        # Save the updated user information
        user = self.request.user
        user.first_name = form.cleaned_data['first_name']
        user.last_name = form.cleaned_data['last_name']
        user.email = form.cleaned_data['email']
        user.save()
        messages.success(self.request, 'Your profile has been updated successfully.')
        return super().form_valid(form)

    def form_invalid(self, form):
        # If the form is invalid, show an error message
        messages.error(self.request, 'There was an error updating your profile.')
        return super().form_invalid(form)    