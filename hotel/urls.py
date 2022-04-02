from django.urls import path

from . import views

app_name = 'hotel'

urlpatterns = [
    path('rooms/', views.RoomList.as_view(), name='room-list'),
    path('bookings/', views.BookingList.as_view(), name='booking-list'),
    path('book/', views.BookingForm.as_view(), name='book-form')
]