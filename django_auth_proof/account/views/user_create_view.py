from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.views.generic.edit import CreateView
from django_auth_proof.account.forms import UserCreationForm

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = 'user_create.html'
    
    def form_valid(self, form):
        valid = super(UserCreateView, self).form_valid(form)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        
        if user := authenticate(username=username, password=password):
            login(self.request, user)
        return valid

    def get_success_url(self):
        return reverse('account:profile', kwargs={'username': self.object.username})
    