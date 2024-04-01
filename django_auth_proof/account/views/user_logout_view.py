from django.views import View
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy

class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse_lazy('account:login'))