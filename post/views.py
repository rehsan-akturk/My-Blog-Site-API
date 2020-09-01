from django.shortcuts import render,redirect,HttpResponse,get_object_or_404,reverse
from post.models import Post,Comment,Category
from django.views import generic
from django.contrib.auth.models import User
from post.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage
from rest_framework import generics
from .serializers import PostSerializer




# Create your views here.

def index(request):
    return render(request,"index.html")




def post(request):
    post=Post.objects.filter(status=1).order_by('created_on')
    return render(request,"postlist.html",{'post':post})


def show_category(request,hierarchy=None):
    category_slug=hierarchy.split('/')
    category_queryset=list(Category.objects.all())
    all_slugs=[x.slug for x in category_queryset]
    parent=None
    for slug in category_slug:
        if slug in all_slugs:
            parent=get_object_or_404(Category,slug=slug,parent=parent)
        
        else:
            instance=get_object_or_404(Post,slug=slug)
            breadcrumbs_link=instance.get_cat_list()
            category_name = [' '.join(i.split('/')[-1].split('-')) for i in breadcrumbs_link]
            breadcrumbs=zip(breadcrumbs_link,category_name)
            return render(request, "postdetail.html", {'instance':instance,'breadcrumbs':breadcrumbs})
    return render(request,"postlist.html",{'post_set':parent.post_set.all(),'sub_categories':parent.children.all()})

    

def postdetail(request,slug):
    post = get_object_or_404(Post ,slug=slug)
    comments = post.comments.all()
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            return redirect(f"/{slug}")
    else:
        comment_form = CommentForm()

    return render(request,'postdetail.html',
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
            

    })






#API

class PostList(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class =PostSerializer


        
    



