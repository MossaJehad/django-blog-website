from django.shortcuts import render # type: ignore
from django.urls import reverse_lazy # type: ignore
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView # type: ignore
from .models import Post

# Create your views here.
class BlogListView(ListView):
	model = Post
	template_name = 'home.html'

class BlogDetailView(DetailView):
	model = Post
	template_name = 'post_details.html'

class BlogCreateView(CreateView):
	model = Post
	template_name = 'post_new.html'
	fields = ['title', 'author', 'body']

	def get_initial(self):
		initial = super().get_initial()
		if self.request.user.is_authenticated:
			initial['author'] = self.request.user
		return initial

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def get_form(self, form_class=None):
		form = super().get_form(form_class)
		form.fields['author'].disabled = True
		return form

class BlogUpdateView(UpdateView):
	model = Post
	template_name = 'post_edit.html'
	fields = ['title', 'body']

class BlogDeleteView(DeleteView): # new
	model = Post
	template_name = 'post_delete.html'
	success_url = reverse_lazy('home')