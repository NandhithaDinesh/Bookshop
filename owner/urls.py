from django.urls import path
from owner import views
urlpatterns=[
    path("category",views.CategoryAddView.as_view(),name="category"),
    path("index", views.AdminDashBoardView.as_view(), name="dashboard"),
    path("book", views.BookAddView.as_view(), name="book"),
    path("book/list", views.BookListView.as_view(), name="book-list"),
    path("category/list", views.CategoryListView.as_view(), name="category-list"),
    path("category/remove/<int:id>", views.delete_category, name="remove-category"),
    path("book/remove/<int:id>", views.delete_book, name="remove-book"),
    path("book/details/<int:id>", views.BookDetailView.as_view(), name="book-detail"),
    path("book/change/<int:id>", views.BookEditView.as_view(), name="edit-book"),
    path("signout", views.SignOutView.as_view(), name="signout"),
    path("category/change/<int:id>", views.CategoryEditView.as_view(), name="edit-category"),

]