#Created Funcgion Based Views
from django.shortcuts import redirect, render
from blogsapp.models import Blog, Category
from ExtraFeatures.models import About
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False, status='Published')
   

   #Fetch About Us  Data
    try:
       about = About.objects.get()
    except:
        about = None

    context = {
       'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
        
        
    }
    return render(request, 'home.html', context)

#For User Registration
def register(request):
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
       # else:
        #   print(form.errors)
    else:
     form = RegistrationForm()
    context ={
        'form': form,

    }
    return render(request, 'register.html',context)

#For Login Page
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = auth.authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})

#For Logout page
def logout(request):
    auth.logout(request)
    return redirect('home')

