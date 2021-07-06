from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate
from .forms import RegisterForm
from .models import Post

# Create your views here.
def user_register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            user=form.save()
            return redirect('user_app:login_user')
    else:
        form=RegisterForm()
    return render(request,"user/register.html",{'form':form})

def login_user(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request,"user/login.html",{'login_form':form})
def logout_user(request):
    logout(request)
    return redirect('/')

def addpost(request):
    if request.method == "POST":
        text = request.POST.get('text')
        post=Post(text=text)
        post.save()
        return redirect('/')
    return render(request, 'user/add.html')

def posts(request):
    item=Post.objects.all()
    return render(request,'user/postdetails.html',{'item':item})
