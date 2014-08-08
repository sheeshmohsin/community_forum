from django.shortcuts import render
# view imports
from django.core.urlresolvers import reverse
from django.views.generic import DetailView
from django.views.generic import RedirectView
from django.views.generic import UpdateView
from django.views.generic import ListView
from allauth.account.views import SignupView, LoginView
# Only authenticated users can access views using this.
from braces.views import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
# Create your views here.

class UserDetailView(LoginRequiredMixin, DetailView):
    model = AbstractUser
    # These next two lines tell the view to index lookups by username
    slug_field = "username"
    slug_url_kwarg = "username"


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail",
            kwargs={"username": self.request.user.username})
