from django import forms
from .models import Venue, VenueAvailability, Booking

class VenueUpdateForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'location', 'capacity', 'manager']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter venue name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter venue location'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter venue capacity'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
        }

class VenueAvailabilityForm(forms.ModelForm):
    class Meta:
        model = VenueAvailability
        fields = ['venue', 'date', 'is_available']
        widgets = {
            'venue': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['venue', 'event_name', 'organizer', 'booking_date', 'attendees']
        widgets = {
            'venue': forms.Select(attrs={'class': 'form-control'}),
            'event_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'booking_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'attendees': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of attendees'}),
        }        


    def clean(self):
        cleaned_data = super().clean()
        venue = cleaned_data.get('venue')
        attendees = cleaned_data.get('attendees')

        if venue and attendees:
            if attendees > venue.capacity:
                raise forms.ValidationError(
                    f"The number of attendees ({attendees}) exceeds the venue's capacity ({venue.capacity})."
                )
        return cleaned_data    