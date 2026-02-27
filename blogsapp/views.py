from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect    
from .models import Blog, Category


# Create your views here.
def posts_by_category(request, category_id):
    # Fetch the category based on the provided category_id  
    posts = Blog.objects.filter(category=category_id, status='Published')
    #use try and except block to handle the case when category does not exist
    #try:
     # category = Category.objects.get(pk=category_id)
    #except:
        #redirect to home page if category does not exist
     #   return redirect('home')
    #use you want show the 404 error page instead of redirecting to home page if category does not exist
    category = get_object_or_404(Category, pk=category_id)    
    context = {
        'posts': posts,
        'category': category,
    }
    return render(request, 'posts_by_category.html', context)
    