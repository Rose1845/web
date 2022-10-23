from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm

# Create your views here.


def register(request):
    if request.user.is_authenicated:
        return redirect('/')


def login(request):
    if request.user.is_authenticated:
        return render(request,'home.html')
    if request.method == 'POST':
        username=request.POST['user']
        password=request.POST['pass']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request.user)
            return redirect('/')
            
        else:
            form= AuthenticationForm(request)
            return render(
                    request,'login.html',
                    {'form',form}
            )
    else:
        form=AuthenticationForm()
        return render(request,'login.html',
        {'form':form}
        )

def logout(request):
    logout(request)
    return redirect('/')
