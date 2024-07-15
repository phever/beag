from django.shortcuts import render
from .functions import default_context


def index(request):
    return render(request, 'index.html', context=default_context({}))
