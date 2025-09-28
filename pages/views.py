from django.shortcuts import render # type: ignore

# Create your views here.
from django.http import HttpResponse # type: ignore

def homePageView(request):
	return HttpResponse('Hello, World!')