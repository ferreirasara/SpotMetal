from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from .models import Search
from .forms import SearchForm
from .util import searchLinks
from django.contrib import messages


def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            bandsLinks = searchLinks(
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
            # bandsLinks = [
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            #     ['bandName', 'spotifyLink'],
            # ]
            # Save in DB
            form.save()
            # redirect to a new URL:
            return render(request, 'index.html', {'bands': bandsLinks, 'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'index.html', {'form': form})


def saveToFile(request):
    return render(request, 'dashboard.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def aboutUs(request):
    return render(request, 'about-us.html')


def results(request):
    return render(request, 'results.html')


def settings(request):
    return render(request, 'settings.html')
