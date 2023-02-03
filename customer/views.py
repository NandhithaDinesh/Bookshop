from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from customer import forms
from owner.models import Books, Carts, Orders


# class HomeView(TemplateView):
#     template_name: str="home.html"
# class BookListView(ListView):
#     model = Books
#     template_name = "home.html"
#     context_object_name = "books"
class HomeView(TemplateView):
    template_name: str="homebody.html"

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        all_books=Books.objects.all()
        context["books"]=all_books


        return context

class BookListView(ListView):
    model = Books
    template_name = "home2.html"
    context_object_name = "books"

class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect("login")

class AddToCartView(FormView):
    template_name: str="addto-cart.html"
    form_class=forms.CartForm

    def get(self, request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        return render(request,self.template_name,{"form":forms.CartForm(),"book":book})
    def post(self,request,*args,**kwargs):
        id=kwargs.get("id")
        book=Books.objects.get(id=id)
        qty=request.POST.get("qty")
        user=request.user
        Carts.objects.create(book=book,
        user=user,
        qty=qty)
        messages.success(request,"Your item has been added to cart!!!!")
        return redirect("books")

class MyCartView(ListView):
    model=Carts
    template_name: str="mycart.html"
    context_object_name="carts"

    def get_queryset(self):
        return Carts.objects.filter(user=self.request.user).order_by("-created_date")
def delete_item(request,*args,**kwargs):
    cart_id=kwargs.get("cid")
    cart=Carts.objects.get(id=cart_id)
    cart.delete()
    cart.status="cancelled"
    cart.save()
    return redirect("mycart")
class PlaceOrderView(FormView):
    template_name: str="placeorder.html"
    form_class=forms.OrderForm

    def post(self, request,*args,**kwargs):
        cart_id=kwargs.get("cid")
        book_id=kwargs.get("bid")
        cart=Carts.objects.get(id=cart_id)
        book=Books.objects.get(id=book_id)
        user=request.user
        delivery_address=request.POST.get("delivery_address")
        Orders.objects.create(book=book,user=user,delivery_address=delivery_address)
        cart.status="order-placed"
        cart.save()
        return redirect("mycart")
