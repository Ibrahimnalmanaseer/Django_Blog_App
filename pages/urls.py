from django.urls import path

from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("blog/create", NewBlog.as_view(), name="blog_create"),
    path("blog/<pk>", BlogDetail.as_view(), name="blog_detail"),
    path("blog/update/<pk>",UpdateBlog.as_view(), name="blog_update"),
    path('delete/<id>',delete_blog,name='delete')
]
