from django.shortcuts import render

# Create your views here.

def page(request):
    return render(request,'home.html',{'s':'kalam.jpg'})

