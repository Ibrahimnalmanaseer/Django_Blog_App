from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView
from .models import *
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from .urls import *
class HomePageView(ListView):
    
    model=Blog
    template_name = "pages/home.html"
    
def delete_blog(request,id):
        blog=Blog.objects.get(id=id)
        blog.delete()
        
        return HttpResponseRedirect(reverse('home'))

class AboutPageView(TemplateView):
    template_name = "pages/about.html"



class BlogDetail(DetailView):

    model=Blog
    template_name='pages/blog_detail.html'


class BlogForm(forms.ModelForm):

    class Meta:
        model =Blog
        fields = ['title','body','author','image']
        widgets = {
        'title': forms.TextInput(attrs={'class':"form-control", 'type':"text" ,}),
        'body': forms.Textarea(attrs={'class':"form-control", 'type':"text" ,}),
        
           }
class NewBlog(CreateView):

    template_name='pages/new_blog.html'
    model=Blog
    form_class=BlogForm


class UpdateBlog(UpdateView):

    template_name='pages/update_blog.html'
    model=Blog
    form_class=BlogForm