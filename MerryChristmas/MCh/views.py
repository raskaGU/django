from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
# Create your views here.
def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html' ,
                  {"posts": posts,
                  "title": "Главная страница"})


def about(request):
    return HttpResponse("<h1>Это страница о нас!</h1>")


def create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
    form = PostForm()
    content = {"form": form}
    return render(request, 'create.html', content)