from django.shortcuts import render
from .functions import default_context


def index(request):
    context = {
        'title': 'Welcome to Beag - a Dark Ages Wiki'
    }
    return render(request, 'index.html', context=default_context(context, request.path))
