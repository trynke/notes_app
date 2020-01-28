from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .forms import UserRegistrationForm, PostForm
from .models import Note


@login_required
def board(request):
    user = request.user
    notes = Note.objects.filter(author=user)
    return render(request, 'account/board.html', {'notes': notes})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


@login_required
def note_detail(request, pk):
    note = get_object_or_404(Note, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=note)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.created_date = timezone.now()
            note.save()
            return redirect('board')
    else:
        form = PostForm(instance=note)
    return render(request, 'account/note_edit.html', {'form': form})


@login_required
def note_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.published_date = timezone.now()
            note.save()
            return redirect('board')
    else:
        form = PostForm()
    return render(request, 'account/note_edit.html', {'form': form})
