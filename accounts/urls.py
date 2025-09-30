# accounts/urls.py
from django.urls import path # type: ignore
from . import views

urlpatterns = [
	path('signup/', views.SignUpView.as_view(), name='signup'),
]