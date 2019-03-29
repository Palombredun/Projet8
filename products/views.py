from django.shortcuts import render, reverse_lazy
fromd django.views import generic

from .forms import RegistrationForm


class signup(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'