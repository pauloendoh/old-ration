from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from models import Item, User_Item

class SignUpForm(UserCreationForm): #our SignUpForm extends UserCreationForm, which is a ModelForm for creating a new user. A ModelForm is a class for mapping a model class's fields to HTML form <input> elements via a Form .
    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

    def clean_email(self):
        # Get the email
        email = self.cleaned_data.get('email')

        # Check if email is already in use
        try:
            match = User.objects.get(email=email)
        except User.DoesNotExist:
            return email

        raise forms.ValidationError('This email address is already in use.')


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'description', 'type', 'image')

class UserItemForm(forms.ModelForm):
    class Meta:
        model = User_Item
        fields = ('rating','interest' )