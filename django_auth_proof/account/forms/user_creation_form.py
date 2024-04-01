from django.contrib.auth.forms import UserCreationForm as Form
from django_auth_proof.account.models import User


class UserCreationForm(Form):
    class Meta(Form.Meta):
        model = User
        fields = Form.Meta.fields + ('first_name', 'last_name', 'email', 'profile',)
