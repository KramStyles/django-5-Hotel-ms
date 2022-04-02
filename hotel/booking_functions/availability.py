import datetime
from hotel.models import Booking, Room


def check_availability(room, check_in):
    available = Booking.objects.filter(room=room, check_out__lte=check_in)
    return available