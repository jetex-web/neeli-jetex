from django import forms 
from django.forms import ModelForm
from .models import Rent, Hire

class DateInput(forms.DateInput):
    input_type = 'date'

meme = [
    ('Rent Item', 'Rent Item'),
    ('Books', 'Books'),
    ('Vehicle', 'Vehicle'),
    ('House', 'House'),
    ('Things', 'Things'),
]

give_take = [
    ('Give or Take', 'Give or Take'),
    ('Give', 'Give'),
    ('Take', 'Take'),
    ]



class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = "__all__"  
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),
            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Email'
                }),

            'rent_item': forms.Select(choices= meme, attrs = {
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),

            'status': forms.Select(choices= give_take, attrs = {
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),

                        

            'its_name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name - Ex: Harrypotter, Bike, Apartment'
                }),

            'contact_no': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Contact number'
                }),

            'start_date': DateInput(),

            'end_date':   DateInput(),
            'address': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Address'
                }),
        }

service_types = [
    ('Select requirement', 'Select requriement'),
    ('Plumber', 'Plumber'),
    ('Painter', 'Painter'),
    ('Electrician', 'Electrician'),
]


class HireForm(ModelForm):
    class Meta:
        model = Hire
        fields = "__all__"  
        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': "form-control",
                'style': 'max-width: 300px;',
                'placeholder': 'Name'
                }),

            'email': forms.EmailInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Enter Email'
                }),

            'service': forms.Select(choices= service_types , attrs = {
                'class': "form-control",
                'style': 'max-width: 300px;',
                }),

            'contact_no': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Contact number'
                }),

            'date_needed': DateInput(),
            
            'address': forms.TextInput(attrs={
                'class': "form-control", 
                'style': 'max-width: 300px;',
                'placeholder': 'Address'
                }),
        }




