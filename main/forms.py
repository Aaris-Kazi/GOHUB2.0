
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class NewUserForm(UserCreationForm):
    username = forms.CharField(max_length=255, required=True)
    email = forms.EmailField(max_length=255, required=True)
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def save(self, commit = True):
        user = super(NewUserForm, self).save(commit=False)
        
        if commit:
            user.save()    
        return user
