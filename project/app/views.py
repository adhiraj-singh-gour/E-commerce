from django.shortcuts import render
from .models import User

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