from django.shortcuts import render
from django.views import generic

from .models import Booking, Room


class RoomList(generic.ListView):
    model = Room


class BookingList(generic.ListView):
    model = Booking
