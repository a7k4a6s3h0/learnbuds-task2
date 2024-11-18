from django.urls import path
from . import views

urlpatterns = [
    path('attendee_home/', views.AttendeeHomePageView.as_view(), name='attendee_home'),
    path('register-event/<int:event_id>/', views.RegisterEventView.as_view(), name='register_event'),
    path('update-registration/<int:registration_id>/', views.UpdateRegistrationView.as_view(), name='update_registration'),
    path('delete_registration/<int:event_id>/', views.DeleteRegistrationView.as_view(), name='delete_registration'),
     path('update-profile/', views.UpdateProfileView.as_view(), name='update_profile'),
]
