from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("This is my first view page")
