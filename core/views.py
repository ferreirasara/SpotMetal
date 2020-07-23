from django.shortcuts import render
from .models import Status

def index(request):
    status = Status.objects.all()

    context = {
        'status': status
    }

    return render(request, 'index.html', context)


def dashboard(request):
    return render(request, 'dashboard.html')


def settings(request):
    return render(request, 'settings.html')
