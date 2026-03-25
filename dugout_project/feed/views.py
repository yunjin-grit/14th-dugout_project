from django.shortcuts import render, redirect
from .forms import PostModelForm

# Create your views here.
def feed(request):
		return render(request, "projects.html")

def create(request):
    if request.method == 'POST':
        form = PostModelForm(request.POST)  
        if form.is_valid():  
            form.save() 
            return redirect('feed') 
    else:
        form = PostModelForm()  
    return render(request, 'form_create.html', {'form': form})