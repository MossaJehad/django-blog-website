from django.urls import path # type: ignore
from .views import homePageView

urlpatterns = [
	path('', homePageView, name='home')
]