from django.shortcuts import render,redirect
from post.models import Post
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title,content=content)
        return redirect('/post/read/?post_id=%s' % post.id)
    return render(request, "create_post.html", {})
def edit_post(request):
    # 是对数据的修改过程，必须带id确定被修改的对象
    if request.method == 'POST':
        post_id = int(request.POST.get("post_id"))
        post = Post.objects.get(id = post_id)
        title = request.POST.get("title")
        content = request.POST.get("content")
        post.title = title
        post.content = content
        post.save()
        return redirect('/post/read/?post_id=%s' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(id = post_id)
        return render(request, "edit_post.html", {'post': post})

def read_post(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(id=post_id)
    return render(request, "read_post.html", {'post':post})

def post_list(request):
    return render(request, "post_list.html", {})

def search(request):
    return render(request, "search.html", {})

