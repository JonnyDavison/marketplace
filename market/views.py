from django.shortcuts import render


def index(request):
    """ a view to retuern the index page """
    return render(request, 'market/index.html')