from django.shortcuts import render
from django.contrib.auth import  get_user_model
from .forms import RegisterForm
from django.views import generic
from products.models import Film


User = get_user_model()

# Create your views here.

def home_view(request):
    context ={
            
    }
    return render(request,'index.html', context)


def register_view(request):
    form = RegisterForm(request.POST or None)
    context ={
            'form':form
    }
    if form.is_valid():
        print (form.cleaned_data)
        username = form.cleaned_data.get("username")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        User.objects.create_user(username, email, password)
    return render(request,"register.html",context)

class FilmListView(generic.ListView):
    model = Film
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(FilmListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        #context['some_data'] = 'This is just some data'        
        return context
class FilmDetailView(generic.DetailView):
    model = Film
    