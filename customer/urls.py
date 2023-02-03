from django.urls import path
from customer import views

urlpatterns=[
    # path("home", views.HomeView.as_view(), name="home"),
    path("home", views.HomeView.as_view(), name="home"),
    path("home/books", views.BookListView.as_view(), name="books"),
    path("signout", views.SignOutView.as_view(), name="signout"),
    path("book/<int:id>/carts/add", views.AddToCartView.as_view(), name="addto-cart"),
    path("carts/all", views.MyCartView.as_view(), name="mycart"),
    path("carts/remove/<int:cid>", views.delete_item, name="remove-item"),
    path("carts/placeorder/<int:cid>/<int:bid>", views.PlaceOrderView.as_view(), name="place-order"),

]