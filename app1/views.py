
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm

# Create your views here.

def home(request):
    return render(request,'main/home.html')


def register(request):
    if request.user.is_authenicated:
        return redirect('/')
    if request.method == 'POST':
        form=UserCreationForm(request)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email=form.cleaned_data.get('email')

            user = authenticate(username=username,password=password,email=email)

            login(request,user)
            return redirect('/')

        else:
            return render(
                request,
                'main/register.html',
                {'form':form}
            )



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
                    request,'main/login.html',
                    {'form',form}
            )
    else:
        form=AuthenticationForm()
        return render(request,'main/login.html',
        {'form':form}
        )

def logout(request):
    logout(request)
    return redirect('/')
