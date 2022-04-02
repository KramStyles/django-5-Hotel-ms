from django.shortcuts import render
from django.views import generic

from .forms import FormAvailability
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


class BookingForm(generic.FormView):
    form_class = FormAvailability
    template_name = 'hotel/booking_form.html'

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        print(room_list)
