from django import forms
from django.contrib import admin
from .models import User


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ['password']

    
class UserAdmin(admin.ModelAdmin):
    form = UserForm