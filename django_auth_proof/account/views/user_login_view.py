from django.contrib.auth.views import LoginView as Login
from django.http import HttpResponseRedirect
from django.urls import reverse


class LoginView(Login):
    template_name = 'user_login.html'
    
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_default_redirect_url())
        return super().get(request, *args, **kwargs)

    def get_default_redirect_url(self):
        return reverse('account:profile', kwargs={'username': self.request.user.username})
