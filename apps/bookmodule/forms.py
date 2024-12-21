from django import forms
from .models import Book
from .models import Student, Address
from .models import Student2, Address2
from .models import ImageModel


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'address']


class Address2Form(forms.ModelForm):
    class Meta:
        model = Address2
        fields = ['city']

class Student2Form(forms.ModelForm):
    class Meta:
        model = Student2
        fields = ['name', 'age', 'addresses']
        widgets = {
            'addresses': forms.CheckboxSelectMultiple,  # Allow selecting multiple addresses
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = ['title', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter image title'}),
        }