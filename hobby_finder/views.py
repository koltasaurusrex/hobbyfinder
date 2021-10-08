from django.shortcuts import (
    HttpResponseRedirect,
   	get_object_or_404,
    render
)
from django.contrib.auth.forms import UserCreationForm


def homepage(request):
    if request.user.is_authenticated:
        return render(request, 'events.html')
    else:
        return render(request, 'base.html')


def hobby(request):
    return render(request, 'hobby.html')


def events(request):
    return render(request, 'events.html')


def registerPage(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'registration.html', context)
