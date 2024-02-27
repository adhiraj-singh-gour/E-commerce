from django.shortcuts import render
from .models import *
from .forms import Product

# Create your views here.
def home(request):
    data = Products.objects.filter(Type="tshirt")
    data1 = Products.objects.filter(Type="shoes")
    data2 = Products.objects.filter(Type="glasses")
    return render(request, "home.html", {"ts": data,"sh":data1,"sg":data2})



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


def product(request,pk):
    
    data = Products.objects.get(id=pk)
    
    return render(request,'productDetail.html', {"data": data})

def cart(request,pk):
    card = request.session.get('card',[])
    card.append(pk)
    request.session['card'] = card
    print(card)
    data = Products.objects.get(id=pk)
    return render(request,'productDetail.html', {"data": data})


def adminpage(request):
    return render(request,'admin.html')


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
