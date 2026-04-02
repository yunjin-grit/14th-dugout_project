from django.shortcuts import render, redirect
from .forms import NoticeModelForm

# Create your views here.
def main(request):
		return render(request, "index.html")
