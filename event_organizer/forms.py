from django import forms
from .models import Event, Venue

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'status', 'date', 'time', 'venue']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter event description', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'venue': forms.Select(attrs={'class': 'form-control'}),
        }



class VenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ['name', 'location', 'capacity', 'manager']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter venue name'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter venue location'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter venue capacity'}),
            'manager': forms.Select(attrs={'class': 'form-control'}),
        }



class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'status', 'date', 'time', 'venue']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter event name'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter event description', 'rows': 4}),
            'status': forms.Select(attrs={'class': 'form-control'}),  # Dropdown for status
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'venue': forms.Select(attrs={'class': 'form-control'}),
        }
