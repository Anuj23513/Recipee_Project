from django.shortcuts import render,redirect
from .models import *


# Create your views here.

def home(request):
    if request.method=='POST':
        form=request.POST
        name=form.get('name')
        description=form.get('description')
        image=request.FILES.get('image')
        
        
        Recipee.objects.create(
            name=name,
            description=description,
            image=image,
            
        )
        return redirect('/')
         
    Recipees=Recipee.objects.all()
    context={'Recipees':Recipees}
    return render(request,'index.html',context)


def login(request):
    return render(request,'login.html')
