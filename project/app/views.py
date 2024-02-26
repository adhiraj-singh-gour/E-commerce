from django.shortcuts import render
from .models import *
from .forms import Product

# Create your views here.
def home(request):
    return render(request,'home.html')


def contact(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    

    User.objects.create(
        Name = name,
        Email = email,
        Message = message
    )
    msg = "Send Successfully"
    return render(request,'home.html',{"msg":msg})


def product(request):
    return render(request,'productDetail.html')


def pro_detail(request):
    if request.method == "POST":
        form = Product(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
    form = Product()
    return render(request, "add.html", {"form": form})


def show(request):
    data = Products.objects.all()
    return render(request, "show.html", {"data": data})
