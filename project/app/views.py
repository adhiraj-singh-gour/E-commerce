from django.shortcuts import render,redirect
from .models import *
from .forms import *

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
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email,password)
        # Checking the emailid with database
        user = Signup.objects.filter(email=email)
        if user:
            data = Signup.objects.get(email=email)
            if data.password == password:
                id  = data.id
                username = data.username
                email = data.email
                password = data.password
                request.session['id']=id
                request.session['name']=username
                request.session['email']=email
                user={
                    'name':username,
                    'email':email,
                    'password':password,
                }
                data = Products.objects.filter(Type="tshirt")
                data1 = Products.objects.filter(Type="shoes")
                data2 = Products.objects.filter(Type="glasses")
                return render(request,"user.html",{"user":user,"ts": data,"sh":data1,"sg":data2})
            else:
                message = "Password does not match"
                return render(request,"signin.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"signup.html",{'msg':message})


def logout(request):
    
    del request.session['id']
    del request.session['name']
    del request.session['email']
    request.session.flush()

    return redirect('home')

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
    card = request.session['card']
    data = {}
    key = 1
    sum = 0
    items = 0
    for i in card:
        data[key] = Products.objects.get(id=i)
        sum = sum + data[key].Price
        key+=1
    items += len(data.keys())
    return render(request,'cart.html', {"data": data.values,'sum':sum,'items':items})
    
def remove(request,pk):
     card = request.session['card']
     card.remove(pk)
     request.session['card'] = card
     return redirect('/cart')
     
def checkout(request):
    card = request.session['card']
    data = {}
    key = 1
    sum = 0
    items = 0
    for i in card:
        data[key] = Products.objects.get(id=i)
        sum = sum + data[key].Price
        key+=1
    items += len(data.keys())
    username = request.session['name']
    email=request.session['email']
    return render(request,'checkout.html',{"data": data.values,'sum':sum,'items':items,'username':username, 'email':email})     

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







# Create your views here.
import razorpay
from django.views.decorators.csrf import csrf_exempt

def item_payment(request):
    if request.method=="POST":
        name = request.POST.get('name')
        print(name)
        amount = float(request.POST.get('amount')) * 100
        print(amount)
        client = razorpay.Client(auth=("rzp_test_ank5gb82ed6Jfx","jPpRlGXIaMvgyrlcb1gXuEoV"))
        response_payment = client.order.create({'amount':amount, 'currency':'INR','payment_capture':'1' })
    
        print(response_payment)
        order_status = response_payment['status']
        order_id = response_payment['id']
        
        if order_status=='created':
            product = ItemModel(name=name , amount =amount , order_id = response_payment['id'])
            product.save()
            response_payment['name'] = name
            fm = PaymentForm( request.POST or None)
            return render(request,'payment.html',{'form':fm,'payment':response_payment})

    fm = PaymentForm()
    return render(request,'payment.html',{'form':fm})