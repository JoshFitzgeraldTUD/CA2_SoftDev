from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.contrib.auth.models import Group

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        group = forms.ModelChoiceField(queryset=Group.objects.all(), required=True)
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('age','email',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields 