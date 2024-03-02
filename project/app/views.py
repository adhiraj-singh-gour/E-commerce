from django.shortcuts import render
from .models import *
from .forms import Product

# Create your views here.
def home(request):
    data = Products.objects.filter(Type="tshirt")
    data1 = Products.objects.filter(Type="shoes")
    data2 = Products.objects.filter(Type="glasses")
    return render(request, "home.html", {"ts": data,"sh":data1,"sg":data2})

def signup(request):
    return render(request, "signup.html")
    
def signin(request):
    return render(request, "signin.html")

def usersignup(request):
    if request.method == "POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')
        user = Signup.objects.filter(email=email)

        if user:
            message = "User already exist"
            return render(request, "signup.html", {"msg": message})
        else:
            if password == cpassword:
                newuser = Signup.objects.create(
                    username=username,
                    email=email,
                    password=password,
                    Cpassword=cpassword
                )
                message = "User register Successfully"
                return render(request, "signin.html", {"msg": message})
            else:
                message = "Password and Confirm Password Does not Match"
                return render(request, "signup.html", {"msg": message})
            


def usersignin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        # Checking the emailid with database
        user = Signup.objects.filter(username=username)
        if user:
            data = Signup.objects.get(username=username)
            if data.password == password:
                username = data.username
                email = data.email
                password = data.password
                user = {
                    "username": username,
                    "email": email,
                    "password": password,
                }
                return render(request, "home.html", user)
            else:
                message = "Password does not match"
                return render(request, "login.html", {"msg": message})
        else:
            message = "User does not exist"
            return render(request, "register.html", {"msg": message})



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

def cart(request):
    return render(request,'cart.html')

def add_cart(request,pk):
    card = request.session.get('card',[])
    card.append(pk)
    request.session['card'] = card
    print(card)
    data = Products.objects.get(id=pk)
    return render(request,'productDetail.html', {"data": data})

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




# admin pannel
def adminpage(request):
    data = Products.objects.all()
    return render(request,'admin.html',{'data':data})

def viewuser(request):
    user = Signup.objects.all()
    return render(request,'viewuser.html',{'user':user})

def update(request,pk):
    data = Products.objects.get(id=pk)
    return render(request,'add.html',{'data':data})

def update_product(request):
    if request.method == "POST":
        form = Product(request.POST, request.FILES)
        if form.is_valid():
            form.save() 
    form = Product()
    return render(request, "update.html", {"form": form})

def delete(request, pk):
    data = Products.objects.get(id=pk)
    data.delete()
    data=Products.objects.all()
    return render(request,'admin.html')
