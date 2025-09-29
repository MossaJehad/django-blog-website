from django.shortcuts import render # type: ignore
from django.views.generic import ListView, DetailView # type: ignore
from .models import Post

# Create your views here.
class BlogListView(ListView):
	model = Post
	template_name = 'home.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_details.html'