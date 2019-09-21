from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import GuestBook
from webapp.forms import GuestBookForm


def book_view(request, *args, **kwargs):
    articles = GuestBook.objects.filter(status='active').order_by('-date_of_creation')
    context = {
        'articles': articles
    }
    return render(request, 'index.html', context)


def add_guest(request):
    if request.method == 'GET':
        form = GuestBookForm()
        return render(request, 'guest_add.html', context={'form': form})
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            GuestBook.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                text=form.cleaned_data['text']
            )
            return redirect('index')
        else:
            return render(request, 'guest_add.html', context={'form': form})
