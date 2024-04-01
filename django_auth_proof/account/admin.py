from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django_auth_proof.account.models import User
from django_auth_proof.account.forms import UserChangeForm, UserCreationForm

@admin.register(User)
class UserAdmin(AuthUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    model = User
    fieldsets = AuthUserAdmin.fieldsets + (('profile', {'fields': ('profile',)}),)