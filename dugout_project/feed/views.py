from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm
from main.models import Notice

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

def feed_list(request):
    feed = Notice.objects.all().order_by('-created_at')
    return render(request, "feed_list.html", {"feed" : feed})

def feed_detail(request, feed_id):
    feed = get_object_or_404(Notice, pk=feed_id)
    return render(request, "feed_detail.html", {"feed":feed})

def feed_update(request, id):
    post = get_object_or_404(Notice, pk=id)

    if request.method == 'POST':
        form = PostModelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed_list')
    else:  
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'feed_id':id})
    
def feed_delete(request, id):
       feed = Notice.objects.get(pk=id)
       feed.delete()
       return redirect('feed_list')