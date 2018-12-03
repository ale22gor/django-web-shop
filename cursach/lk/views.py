from django.shortcuts import render
from django.contrib.auth import authenticate, login, get_user_model
from .forms import RegisterForm, LoginForm, UserEditForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
User = get_user_model()

# Create your views here.
def home_view(request):
    context ={
            
    }
    return render(request,'account/home.html', context)

def login_view(request):
    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username = cd['username'], password = cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated succsefully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

def register_view(request):
    if request.POST:
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            username = user_form.cleaned_data.get("username")
            email = user_form.cleaned_data.get("email")
            password = user_form.cleaned_data.get("password")
            user = User.objects.create_user(username, email, password)
            return render(request, 'account/register_done.html', {'new_user': user})
    else:        
        user_form = RegisterForm()
    return render(request,'account/register.html',{'user_form': user_form})


@login_required
def edit_view(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        if user_form.is_valid() :
            
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    return render(request,'account/edit.html',{'user_form': user_form})