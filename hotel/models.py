from django.db import models


class Room(models.Model):
    room_categories = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('QUE', 'QUEENS'),
        ('KIN', 'KINGS')
    )
    number = models.IntegerField()
    beds = models.IntegerField()
    capacity = models.IntegerField()
    category = models.CharField(max_length=10, choices=room_categories)

    def __str__(self):
        return f'{self.number}, {self.category} with {self.beds} for {self.capacity} people'
