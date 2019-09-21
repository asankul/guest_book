from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import GuestBook


def book_view(request, *args, **kwargs):
    articles = GuestBook.objects.filter(status='active').order_by('-date_of_creation')
    context = {
         'articles': articles
     }
    return render(request, 'index.html', context)
