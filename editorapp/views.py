from django.shortcuts import render
from .models import Post
from .forms import PostForm

# Create your views here.

def index(request):
    myfrm = PostForm()
    return render(request,'index.html',{'myfrm':myfrm})
