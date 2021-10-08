from django.shortcuts import render,redirect
from .models import Category, Myphoto

# Create your views here.
def gallery(request):
    category=request.GET.get('category')

    if category==None:
        photos=Myphoto.objects.all()
    else:
       photos=Myphoto.objects.filter(category__name=category) 

    categories=Category.objects.all()
    

    context={'categories':categories,'photos':photos}

    return render(request, 'photos/gallery.html',context)
    
def viewPhoto(request,pk):
    photo=Myphoto.objects.get(id=pk)

    return render(request, 'photos/photo.html',{'photo':photo})

def newPhoto(request):
    categories=Category.objects.all()

    if request.method =='POST':
        data=request.POST
        image=request.FILES.get('image')
        if data['category'] != 'none':
            category= Category.objects.get(id=data['category']) 
        elif data['new_category'] != '':
            category,created=Category.objects.get_or_create(name=data['new_category'])
        else:
            category=None    
        photo=Myphoto.objects.create(
            category=category,
            description=data['description'],
            image=image
        ) 
        return redirect('gallery')
    context={'categories':categories}
    return render(request, 'photos/newphoto.html', context)