from django import forms
from .models import Room


class FormAvailability(forms.Form):
    room_categories = Room.room_categories
    room_category = forms.ChoiceField(choices=room_categories, required=True)
    check_in = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M'])
    check_out = forms.DateTimeField(required=True, input_formats=['%Y-%m-%dT%H:%M'])
