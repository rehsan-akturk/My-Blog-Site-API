from django.urls import path,include
from django.contrib import admin
from post import views

app_name = "post"


urlpatterns = [
    
    path('', views.index, name='index'),
    path('api/', views.PostList.as_view()),
    path('api/<int:pk>/', views.PostDetail.as_view()),
    path('ssl/', views.post, name='post'),
    path('ssl/<path:hierarchy>/', views.show_category,name='category'),
    path('<slug:slug>/', views.postdetail,name='postdetail'),
    
]
    
   
    
  

