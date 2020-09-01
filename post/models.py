from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse
from ckeditor.fields import RichTextField
    


# Create your models here.
    
class Category(models.Model):
    name=models.CharField(max_length=250)
    slug=models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True ,on_delete= models.CASCADE,related_name='children')
    

    class Meta:
        ordering=['-name']
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'categories'
    
    def __str__(self):
        full_path = [self.name]                  
        k = self.parent
        while k is not None:
            full_path.append(k.name)
            k = k.parent
        return ' -> '.join(full_path[::-1])
    



STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    category=models.ForeignKey(Category,on_delete= models.CASCADE,related_name='post_set')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextField(blank=True) #CKEditör
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    thumb=models.ImageField(default='default.png',blank=True)
   


    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    def get_cat_list(self):
        k = self.category
        breadcrumb = ["dummy"]
        while k is not None:
            breadcrumb.append(k.slug)
            k = k.parent
        for i in range(len(breadcrumb)-1):
            breadcrumb[i] = '/'.join(breadcrumb[-1:i-1:-1])
        return breadcrumb[-1:0:-1]


    def get_absolute_url(self):
      return reverse('post:postdetail', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        self.slug = self.slug or slugify(self.title)
        super().save(*args, **kwargs) 




class Comment(models.Model):
    
    post = models.ForeignKey(Post,on_delete = models.CASCADE,verbose_name = "Makale",related_name="comments")
    comment_author = models.CharField(max_length = 50,verbose_name = "İsim")
    comment_content = models.CharField(max_length = 200,verbose_name = "Yorum")
    comment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment_content

    class Meta:
        ordering = ["-comment_date"]




    
   

