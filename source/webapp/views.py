from django.shortcuts import render, get_object_or_404, redirect
from webapp.models import GuestBook
from webapp.forms import GuestBookForm


def book_view(request, *args, **kwargs):
    guest_book = GuestBook.objects.filter(status='active').order_by('-date_of_creation')
    context = {
        'guest_book': guest_book
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


def edit_guest(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = GuestBookForm(data={
            'name': guest_book.name,
            'email': guest_book.email,
            'text': guest_book.text
        })
        return render(request, 'guest_edit.html', context={'form': form, 'guest_book': guest_book})
    elif request.method == 'POST':
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guest_book.name = form.cleaned_data['name']
            guest_book.email = form.cleaned_data['email']
            guest_book.text = form.cleaned_data['text']
            guest_book.save()
            return redirect('index')
        else:
            return render(request, 'guest_edit.html', context={'form': form, 'article': guest_book})


def delete_guest(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, 'guest_delete.html', context={'guest_book': guest_book})
    elif request.method == 'POST':
        guest_book.delete()
        return redirect('index')
