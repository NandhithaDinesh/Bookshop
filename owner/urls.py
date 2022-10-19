from django.urls import path
from owner import views
urlpatterns=[
    path("category",views.CategoryAddView.as_view(),name="category"),
    path("index", views.AdminDashBoardView.as_view(), name="dashboard"),
    path("book", views.BookAddView.as_view(), name="book"),

]