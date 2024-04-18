from django.shortcuts import render
from django.views.generic import CreateView

from myauth.forms import MyUserCreateForm
from myauth.models import MyUser


# Create your views here.
class MyUserCreateView(CreateView):
    model = MyUser
    success_url = '/'
    form_class = MyUserCreateForm
    # fields = ('username', 'email', 'password1', 'password2')