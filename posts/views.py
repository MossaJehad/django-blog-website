from django.shortcuts import render # type: ignore

def posts_home(request):
	from .models import Post
	posts = Post.objects.all()
	return render(request, "posts/posts_home.html", {"posts": posts})
