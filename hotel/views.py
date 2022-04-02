from django.shortcuts import render, HttpResponse
from django.views import generic

from .forms import FormAvailability
from .models import Booking, Room
from .booking_functions.availability import check_availability


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
        check_in = data['check_in']
        category = data['room_category']
        room_list = Room.objects.filter(category=category)
        rooms = [room for room in room_list if check_availability(room, check_in)]
        if rooms:
            room = rooms[0]
            booking = Booking.objects.create(
                user=self.request.user, room=room, check_in=check_in, check_out=data['check_out']
            )
            booking.save()
            return HttpResponse("Room has been booked")
        else: return HttpResponse("Please try another Category")

