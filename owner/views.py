from django.contrib import messages
from django.urls import reverse_lazy

from owner import forms
from django.shortcuts import render
from django.views.generic import FormView, CreateView, TemplateView
from owner.forms import CategoryForm
from owner.models import Categories, Books


class CategoryAddView(CreateView):
    model=Categories
    form_class = forms.CategoryForm
    template_name: str="add-category.html"

    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):

        messages.success(self.request,"your account has been created")
        return super().form_valid(form)
class AdminDashBoardView(TemplateView):
    template_name: str="admin-homepage.html"

class BookAddView(CreateView):
    model=Books
    form_class = forms.BookForm
    template_name: str="add-book.html"

    success_url = reverse_lazy("dashboard")

    def form_valid(self, form):

        messages.success(self.request,"your account has been created")
        return super().form_valid(form)
