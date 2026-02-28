#Created Funcgion Based Views
from django.shortcuts import render
from blogsapp.models import Blog, Category
from ExtraFeatures.models import About

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

