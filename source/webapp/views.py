from django.shortcuts import render, get_object_or_404, redirect
from webapp.forms import EntryForm
from webapp.models import Entry, STATUS_CHOICES


def index_view(request, *args, **kwargs):
    entries = Entry.objects.filter(status=STATUS_CHOICES[0][0]).order_by('-created_at')

    return render(request, "index.html", context={
        'entries': entries
    })


def entry_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    return render(request, "entry.html", context={"entry": entry})


def entry_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = EntryForm()
        return render(request, 'create.html', context={"form": form})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry = Entry.objects.create(
                author=form.cleaned_data["author"],
                email=form.cleaned_data["email"],
                text=form.cleaned_data["text"])
            entry.save()
            return redirect("index")
        else:
            return render(request, "create.html", context={"form": form})


def entry_update_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == 'GET':
        form = EntryForm(data={
            "author": entry.author,
            "email": entry.email,
            "text": entry.text
        })
        return render(request, "update.html", context={"form": form, "entry": entry})
    elif request.method == 'POST':
        form = EntryForm(data=request.POST)
        if form.is_valid():
            entry.author = form.cleaned_data["author"]
            entry.email = form.cleaned_data["email"]
            entry.text = form.cleaned_data["text"]
            entry.save()
            return redirect("index")
        else:
            return render(request, "update.html", context={"form": form, "entry": entry})


def entry_delete_view(request, pk):
    entry = get_object_or_404(Entry, pk=pk)
    if request.method == "GET":
        return render(request, "delete.html", context={"entry": entry})
    elif request.method == "POST":
        entry.delete()
        return redirect("index")
