from django.contrib import messages
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import View

from owner import forms
from django.shortcuts import render, redirect
from django.views.generic import FormView, CreateView, TemplateView, ListView, DetailView, UpdateView
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

class BookAddView(FormView):
    model=Books
    form_class = forms.BookForm
    template_name: str="add-book.html"

    def post(self, request, *args, **kw):
        form = forms.BookForm(request.POST,request.FILES)
        if form.is_valid():
            book_name = form.cleaned_data.get("book_name")
            author = form.cleaned_data.get("author")
            category = form.cleaned_data.get("category")
            image = form.cleaned_data.get("image")
            price = form.cleaned_data.get("price")
            description = form.cleaned_data.get("description")
            obj = Books.objects.create(
                book_name=book_name,
                author= author,
                category=category,
                image=image,
                price=price,
                description=description,

            )
            obj.save()
            return render(request, "admin-homepage.html")
class BookListView(ListView):
    model = Books
    template_name = "booklist.html"
    context_object_name = "books"

class CategoryListView(ListView):
    model = Categories
    template_name = "categorylist.html"
    context_object_name = "categories"

def delete_category(request,*args,**kwargs):
    id=kwargs.get("id")
    Categories.objects.get(id=id).delete()
    return redirect("category-list")
def delete_book(request,*args,**kwargs):
    id=kwargs.get("id")
    Books.objects.get(id=id).delete()
    return redirect("book-list")
class BookDetailView(DetailView):
    model = Books
    context_object_name = "book"
    template_name = "book_details.html"
    pk_url_kwarg = "id"

class BookEditView(UpdateView):
    model = Books
    form_class = forms.BookChangeForm
    template_name = "book_edit.html"
    success_url = reverse_lazy("book-list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, "details has been updated")
        return super().form_valid(form)

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")

class CategoryEditView(UpdateView):
    model = Categories
    form_class = forms.CategoryEditForm
    template_name = "category-edit.html"
    success_url = reverse_lazy("category-list")
    pk_url_kwarg = "id"

    def form_valid(self, form):
        messages.success(self.request, "details has been updated")
        return super().form_valid(form)


