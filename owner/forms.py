from django import forms
from django.forms import ModelForm
from owner.models import Categories, Books


class CategoryForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields=["category_name",
                "is_active"]
        widgets={
            "category_name":forms.TextInput(attrs={"class": "form-control"}),
            "is_active":forms.CheckboxInput()
        }

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=[
            "book_name","author","category","image","price","description"
        ]
        widgets={
            "book_name":forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "category":forms.Select(attrs={"class": "form-control"}),
            "image":forms.ClearableFileInput(attrs={"class": "form-control"}),
            "price":forms.TextInput(attrs={"class": "form-control"}),
            "description":forms.Textarea(attrs={"class": "form-control"}),

        }

class BookChangeForm(forms.ModelForm):
    class Meta:
        model=Books
        fields = [
            "book_name", "author", "category", "image", "price", "description"
        ]
        widgets={
            "book_name":forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control"}),
            "category":forms.Select(attrs={"class": "form-control"}),
            "image":forms.ClearableFileInput(attrs={"class": "form-control"}),
            "price":forms.TextInput(attrs={"class": "form-control"}),
            "description":forms.Textarea(attrs={"class": "form-control"}),

        }

class CategoryEditForm(forms.ModelForm):
    class Meta:
        model=Categories
        fields=["category_name",
                "is_active"]
        widgets={
            "category_name":forms.TextInput(attrs={"class": "form-control"}),
            "is_active":forms.CheckboxInput()
        }


