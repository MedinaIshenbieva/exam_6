from django.urls import path

from webapp.views import (index_view,
                          create_guest_book_view,
                          guest_book_view,
                          guest_book_update_view,
                          guest_book_delete_view)

urlpatterns = [
    path('', index_view, name="index"),
    path('guest_books/add/', create_guest_book_view, name="guest_book_add"),
    path('guest_book/<int:pk>/', guest_book_view, name="guest_book_view"),
    path('guest_book/<int:pk>/update', guest_book_update_view, name="guest_book_update_view"),
    path('guest_book/<int:pk>/delete', guest_book_delete_view, name="guest_book_delete_view")
]
