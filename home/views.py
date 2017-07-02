from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .forms import SignUpForm
from .models import Users
# Create your views here.

def index(request):
    form=SignUpForm()
    return render(request,'home/index.html',{'title':'WebQuiz','form':form,'view':False})

def signup(request):
    form=SignUpForm()
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home/index.html',{'title':'WebQuiz','form':form,'view':False})
        return redirect('/home/signup')
    return render(request,'home/index.html',{'title':'WebQuiz','form':form})

def login(request):
    if request.method=="POST":
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=Users.objects.get(username=username)
        if user.password==password:
            return render(request,'home/index.html',{'title':'WebQuiz','logged':True,'User':username})
        else:
            return HttpResponse("Invalid User")

def logout(request):
    return HttpResponseRedirect('/')



