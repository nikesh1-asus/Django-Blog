from django.contrib import admin
from .models import blog, category    

class blogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'category', 'status', 'is_featured')
    search_fields = ('id','title','category__category_name', 'status')
    serach_filter = ('status', 'is_featured', 'category')
    list_editable = ('is_featured',)



# Register your models here.
admin.site.register(category)
admin.site.register(blog, blogAdmin)
