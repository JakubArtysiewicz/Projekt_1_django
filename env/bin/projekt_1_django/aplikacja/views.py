from django.shortcuts import render, HttpResponse

# Create your views here.
def pierwszastrona(request):
    print(request.user)
    return HttpResponse("<H1>Pierwszastrona<H1> <a href = 'ds/'> <button type='button'> Click Me! </button> </a>")
def drugastrona(request):
    return HttpResponse("<H1>Drugastrona<h1>")