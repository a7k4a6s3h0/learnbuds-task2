

from django.urls import path
from .views import (
     EventOrganizerHome,
     CreateEventView,
     ManageVenueView,
    ManageEventsView,
    ManageAttendeesView,
    AssignVenuesView,
    CreateVenueView,
    UpdateEventView,
    DeleteEventView
)

urlpatterns = [
     path('events_home/', EventOrganizerHome.as_view(), name='events_home'),
     path('create-event/', CreateEventView.as_view(), name='create_event'),
     path('create-venue/', CreateVenueView.as_view(), name='create_venue'),
     path('manage-venue/', ManageVenueView.as_view(), name='manage_venue'),
    path('manage-events/', ManageEventsView.as_view(), name='manage_events'),
    path('update-event/<int:pk>/', UpdateEventView.as_view(), name='update_event'),
    path('delete-event/<int:event_id>/', DeleteEventView, name='delete_event'),

    

    path('manage-attendees/', ManageAttendeesView.as_view(), name='manage_attendees'),
    path('assign-venues/', AssignVenuesView.as_view(), name='assign_venues'),
]

