from django.shortcuts import render
from .models import Category, Myphoto

# Create your views here.
def gallery(request):
    categories=Category.objects.all()
    photos=Myphoto.objects.all()

    mycontext={'categories':categories,'photos':photos}

    return render(request, 'photos/gallery.html',mycontext)
    
def viewPhoto(request,pk):
    return render(request, 'photos/photo.html')

def newPhoto(request):
    return render(request, 'photos/newphoto.html')