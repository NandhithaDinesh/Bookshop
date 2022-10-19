from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy

from loginapp import forms
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView


class LoginView(FormView):
    template_name="login.html"
    form_class=forms.LoginForm

    def post(self, request, *args, **kw):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                if request.user.is_superuser:
                    return redirect("dashboard")
                else:
                    return redirect("home")

            else:
                messages.error(request, "Invalid username or!!!!")

                return render(request, "login.html", {"form": form})


class RegistrationView(CreateView):
    form_class=forms.RegistrationForm
    template_name="registration.html"
    success_url=reverse_lazy("login")

    def form_valid(self, form):
        messages.success(self.request,"your account has been created")
        return super().form_valid(form)

