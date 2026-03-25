from django.shortcuts import render, redirect
from .forms import TeamModelForm

# Create your views here.
def info(request):
		return render(request, "resume.html")

def create(request):
    if request.method == 'POST':
        form = TeamModelForm(request.POST)  
        if form.is_valid():  
            form.save() 
            return redirect('info')  
    else:
        form = TeamModelForm()  
    return render(request, 'form_create.html', {'form': form})