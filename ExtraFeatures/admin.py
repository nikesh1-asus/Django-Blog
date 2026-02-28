from django.contrib import admin
from . models import About, SocialLink


# Register your models here.

#Overwrite the default admin site header and title
class AboutAdmin(admin.ModelAdmin):
   def has_add_permission(self, request):
      count = About.objects.all().count()
      if count == 0:
        return True
      else:
        return False
      

admin.site.register(About, AboutAdmin)

def __str__(self):
    return self.about_heading

admin.site.register(SocialLink)