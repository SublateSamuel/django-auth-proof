from django.views.generic.edit import UpdateView
from django.urls import reverse, reverse_lazy
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

from django_auth_proof.account.models import User
from django_auth_proof.account.forms import UserChangeForm


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserChangeForm
    template_name = 'user_update.html'
    
    def dispatch(self, request, *args, **kwargs):
        if self.kwargs['pk'] != request.user.pk:
            raise Http404()
        return super().dispatch(request, *args, **kwargs)
    
    def get_success_url(self):
        self.object.refresh_from_db()
        return reverse('account:profile', kwargs={'username': self.object.username})
