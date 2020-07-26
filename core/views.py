from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Status
from .forms import SearchForm
from .util import searchLinks


def index(request):
    status = Status.objects.all()

    context = {
        'status': status
    }

    return render(request, 'index.html', context)


def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            bands = searchLinks(
                request.POST.get('bandName'),
                request.POST.get('genre'),
                request.POST.get('country'),
                request.POST.get('status'),
                request.POST.get('yearCreationFrom'),
                request.POST.get('yearCreationTo'),
                request.POST.get('bandNotes'),
                request.POST.get('themes'),
                request.POST.get('location'),
                request.POST.get('bandLabelName')
            )
            # redirect to a new URL:
            return render(request, 'results.html', {'bands': bands})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')


def aboutUs(request):
    return render(request, 'about-us.html')


def results(request):
    return render(request, 'results.html')


def settings(request):
    return render(request, 'settings.html')
