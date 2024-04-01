from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class UserProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'user_profile.html'
    login_url = '/'
    
    def dispatch(self, request, *args, **kwargs):
        if self.kwargs.get('username') != request.user.username:
            return HttpResponseRedirect(reverse('account:login'))
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context