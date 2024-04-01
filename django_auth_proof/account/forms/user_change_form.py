from django import forms
from django.contrib.auth.forms import UserChangeForm as UserChange

from django_auth_proof.account.models import User


class UserChangeForm(UserChange):
    password1 = forms.CharField(label="New password", widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label="New password confirmation", widget=forms.PasswordInput, required=False)
    
    class Meta(UserChange.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'profile',)

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("password1")
        new_password2 = cleaned_data.get("password2")
        
        if new_password1 and new_password2:
            if new_password1 != new_password2:
                self.add_error('password2', "The two password fields didn't match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data["password1"]:
            user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user