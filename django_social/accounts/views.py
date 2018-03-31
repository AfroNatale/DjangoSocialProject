from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import CreateView
from . import forms

# Create your views here.
class Register(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login') #reverse_lazy execute until user hit submit button
    template_name = 'accounts/register.html'
