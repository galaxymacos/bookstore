from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Book


# Create your views here.
class BookListView(LoginRequiredMixin, ListView):
    model = Book
    context_object_name = "book_list"
    template_name = 'books/book_list.html'  # object_list = Book.objects.all()
    login_url = "account_login"  # name


class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'books/book_detail.html'
    login_url = "account_login"  # name
    permission_required = "books.special_status"


class SearchResultsListView(ListView):
    model = Book
    context_object_name = "book_list"
    template_name = "books/search_results.html"
    # queryset = Book.objects.filter(
    #     Q(title__icontains="Death") | Q(title__icontains="Forest")
    # )

    def get_queryset(self):
        # Get called when a get form get submitted
        # Ex: search
        query = self.request.GET.get("q")
        return Book.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )