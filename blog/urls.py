from django.urls import path # type: ignore
from .views import BlogListView, BlogDetailView

urlpatterns = [
	path('post/<int:pk>/', BlogDetailView.as_view(), name='post_details'),
	path('', BlogListView.as_view(), name='home'),
]