from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('document-list')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'users/signup.html', context)
