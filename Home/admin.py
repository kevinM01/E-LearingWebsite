from django.contrib import admin

# Register your models here.
from .models import Contact, faculty, Post

admin.site.register(Contact)



@admin.register(faculty)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'password']



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'file_field']