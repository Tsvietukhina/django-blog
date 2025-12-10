from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from django.shortcuts import get_object_or_404
from .models import Comment
from django.http import HttpResponse


#Posts
def posts(request):

    # Add Post (POST request)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponse("You must be logged in to create posts")
        
        title = request.POST.get('title')
        body = request.POST.get('body')
        image = request.FILES.get('image')

        Post.objects.create(
            title=title,
            body=body,
            image=image,
            author=request.user 
        )

        return redirect('/')
    
    # Show posts (with search filter)
    query = request.GET.get('search')

    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    context = {'posts': posts}
    return render(request, 'posts/posts.html', context)

#Update post
def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.body = request.POST.get('body')

        # update image if a new one is uploaded
        if request.FILES.get('image'):
            post.image = request.FILES.get('image')

        post.save()
        return redirect(f'/post/{id}/')

    return render(request, 'posts/edit_post.html', {'post': post})


#Comments
def post_detail(request, id):
    post = get_object_or_404(Post, id=id)

    # Create comment (POST request)
    if request.method == 'POST':

        if not request.user.is_authenticated:
            return HttpResponse("You must be logged in to comment.")

        text = request.POST.get('text')

        Comment.objects.create(
            post=post,
            text=text,
            author=request.user
        )

        return redirect(f'/post/{id}/')


    comments = post.comments.all().order_by('-created_at')

    return render(request, 'posts/post_detail.html', {
        'post': post,
        'comments': comments
    })

#Delete comment
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)

    # Only author can delete
    if request.user != comment.author:
        return HttpResponse("You are not allowed to delete this comment")

    post_id = comment.post.id
    comment.delete()

    return redirect(f'/post/{post_id}/')

#Delete post
def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.user != post.author:
        return HttpResponse("You are not allowed to delete this post")

    post.delete()
    return redirect('/')
