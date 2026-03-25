from django.shortcuts import render, redirect
from .forms import NoticeModelForm

# Create your views here.
def main(request):
		return render(request, "index.html")

def create(request):
    if request.method == 'POST':
        form = NoticeModelForm(request.POST)  
        if form.is_valid():  
            form.save() 
            return redirect('main')  
    else:
        form = NoticeModelForm()  
    return render(request, 'form_create.html', {'form': form})