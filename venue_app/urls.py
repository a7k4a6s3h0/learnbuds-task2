from django.urls import path
from . import views

urlpatterns = [
    path('venue_home', views.VenueHome.as_view(), name='venue_home'),
    path('update-venue/<int:pk>/', views.VenueUpdateView.as_view(), name='update_venue'),
    path('delete-venue/<int:venue_id>/', views.VenueDeleteView, name='delete_venue'),
    path('availability/', views.ManageAvailabilityView.as_view(), name='manage_availability'),
    path('bookings/', views.ManageBookingsView.as_view(), name='manage_bookings'),
    path('update-booking/<int:pk>/', views.UpdateBookingView.as_view(), name='update_booking'),
    path('delete-booking/<int:booking_id>/', views.DeleteBookingView, name='delete_booking'),
    path('update-availability/<int:pk>/', views.UpdateAvailabilityView.as_view(), name='update_availability'),
    path('delete-availability/<int:availability_id>/', views.AvailabilityDeleteView, name='delete_availability'),
    path('venue_details/<int:venue_id>/', views.VenueMoreDetails.as_view(), name='venue_details'),
]
