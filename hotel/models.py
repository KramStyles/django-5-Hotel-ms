import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Room(models.Model):
    room_categories = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('QUE', 'QUEENS'),
        ('KIN', 'KINGS')
    )
    room_dic = {
        'YAC': 'AC',
        'NAC': 'NON-AC',
        'DEL': 'DELUXE',
        'QUE': 'QUEENS',
        'KIN': 'KINGS'
    }
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity = models.IntegerField()
    category = models.CharField(max_length=10, choices=room_categories)

    def __str__(self):
        return f'Number {self.number} {self.room_dic[self.category]} with {self.beds} bed(s) for {self.capacity} person(s)'


class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField(django.utils.timezone.now())
    check_out = models.DateTimeField()

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'
