from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostModelForm, CommentForm
from .models import Post, Comment
from django.core.paginator import Paginator

# Create your views here.
def feed(request):
		return render(request, "projects.html")

def create(request):
    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES)  
        if form.is_valid():  
            form.save() 
            return redirect('feed_list') 
    else:
        form = PostModelForm()  
    return render(request, 'form_create.html', {'form': form})

def feed_list(request):
    feed = Post.objects.all().order_by('-created_at')
    my_paginator = Paginator(feed, 5)
    page_num = request.GET.get('page')
    posts = my_paginator.get_page(page_num)
    return render(request, "feed_list.html", {"feed" : posts})

def feed_detail(request, feed_id):
    feed = get_object_or_404(Post, pk=feed_id)
    comment_form = CommentForm()
    context = {
        'feed': feed,
        'comment_form': comment_form
    }
    return render(request, "feed_detail.html", context)

def feed_update(request, id):
    post = get_object_or_404(Post, pk=id)

    if request.method == 'POST' or request.method == 'FILES':
        form = PostModelForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('feed_list')
    else:  
        form = PostModelForm(instance=post)
        return render(request, 'form_create.html', {'form':form, 'feed_id':id})
    
def feed_delete(request, id):
       feed = Post.objects.get(pk=id)
       feed.delete()
       return redirect('feed_list')

def create_comment(request, id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.article = get_object_or_404(Post, pk=id)
        finished_form.save()
    return redirect('feed_detail', feed_id=id)

def update_comment(request, post_id, com_id):
    comment = Comment.objects.get(id=com_id)
    
    if request.method == "POST": 
        updated_form = CommentForm(request.POST, instance=comment)
        if updated_form.is_valid():
            updated_form.save()
            return redirect('feed_detail', feed_id=post_id)
    
    else: 
        comment_form = CommentForm(instance=comment)
        context = {'comment_form': comment_form}
        return render(request, 'comment_update.html', context)
    
def delete_comment(request, post_id, com_id):
    comment = Comment.objects.get(id=com_id)
    comment.delete()
    return redirect('feed_detail', feed_id=post_id)