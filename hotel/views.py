from django.shortcuts import render
from django.views import generic

from .models import Booking, Room


class RoomList(generic.ListView):
    model = Room
    context_object_name = 'rooms'

    def get_context_data(self, **kwargs):
        context = super(RoomList, self).get_context_data()
        context['title'] = 'all rooms'
        return context


class BookingList(generic.ListView):
    model = Booking
