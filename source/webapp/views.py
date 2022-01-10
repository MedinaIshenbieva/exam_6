from django.shortcuts import render, redirect, get_object_or_404

from webapp.models import GuestBook, STATUS_CHOICES
from webapp.forms import GuestBookForm


def index_view(request):
    guest_book = GuestBook.objects.order_by("updated_at")
    return render(request, 'index.html', {'guest_book': guest_book})


def create_guest_book_view(request):
    if request.method == 'GET':
        form = GuestBookForm()
        return render(request, 'guest_book_create.html', {"form": form, "status_choices": STATUS_CHOICES})
    else:
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            author = form.cleaned_data.get('author')
            email = form.cleaned_data.get('email')
            text = form.cleaned_data.get('text')
            status = form.cleaned_data.get('status')
            new_guest_book = GuestBook.objects.create(author=author, email=email, text=text, status=status)
            return redirect("guest_book_view", pk=new_guest_book.pk)
        return render(request, 'guest_book_create.html', {"form": form})


def guest_book_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    context = {"guest_book": guest_book}
    return render(request, 'guest_book_view.html', context)


def guest_book_update_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        form = GuestBookForm(initial={
            'author': guest_book.author,
            'email': guest_book.email,
            'text': guest_book.text,
            'status': guest_book.status
        })
        return render(request, 'guest_book_update.html', {"guest_book": guest_book, "form": form})
    else:
        form = GuestBookForm(data=request.POST)
        if form.is_valid():
            guest_book.author = request.POST.get('author')
            guest_book.email = request.POST.get('email')
            guest_book.text = request.POST.get('text')
            guest_book.status = request.POST.get('status')
            guest_book.save()
            return redirect("guest_book_view", pk=guest_book.pk)
        return render(request, 'guest_book_update.html', {"guest_book": guest_book, "form": form})


def guest_book_delete_view(request, pk):
    guest_book = get_object_or_404(GuestBook, pk=pk)
    if request.method == 'GET':
        return render(request, "guest_book_delete.html", {"guest_book": guest_book})
    else:
        guest_book.delete()
        return redirect("index")
