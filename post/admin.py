from django.contrib import admin
from .models import Post,Comment,Category

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    prepopulated_fields={'slug':('name',)}

admin.site.register(Category,CategoryAdmin)



class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'category','status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
  
admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
     list_display=('post','comment_author','comment_content','comment_date')

admin.site.register(Comment,CommentAdmin)




