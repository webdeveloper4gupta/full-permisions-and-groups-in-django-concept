from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,Group
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
    if request.method=='POST':
        n1=request.POST.get('name')
        n2=request.POST.get('password')
        
        user=authenticate(username=n1,password=n2)

        if user is not None:
            login(request,user)
            return render(request,"check.html")
        else:
            messages.error(request,"invalid credentials")
    return render(request,"home.html")
def signout(request):
    logout(request)
    messages.success(request,"Logged out succesfully")
    return redirect('home')


def signup(request):
    if request.method=="POST":
        n1=request.POST.get('n1')
        n2=request.POST.get('n2')
    
        n4=request.POST.get('n4')

        # here do some custom validation
        if User.objects.filter(username=n1):
            messages.error(request,"username already exist")
            return redirect('signup')
        
        if User.objects.filter(email=n2):
            messages.error(request,"already exist ")
            return redirect('signup')
        
        if len(n1)<2:
            messages.error(request,"name must more then 2 character")
            return redirect('signup')
        myuser=User.objects.create_user(n1,n2,n4)
        myuser.save()
       
        group=Group.objects.get(name="editor")
        myuser.groups.add(group)

        messages.success(request,"hurray your  account has been succesfully created.")

        return redirect("home")


    return render(request,"signup.html")
