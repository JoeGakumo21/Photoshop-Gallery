from django.shortcuts import render
from .models import Category, Myphoto

# Create your views here.
def gallery(request):
    categories=Category.objects.all()
    photos=Myphoto.objects.all()

    context={'categories':categories,'photos':photos}

    return render(request, 'photos/gallery.html',context)
    
def viewPhoto(request,pk):
    photo=Myphoto.objects.get(id=pk)

    return render(request, 'photos/photo.html',{'photo':photo})

def newPhoto(request):
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request, 'photos/newphoto.html', context)