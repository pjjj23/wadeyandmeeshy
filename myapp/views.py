from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def gallery(request):
    return render(request, 'gallery.html')

def lily(request):
    return render(request, 'lily.html')