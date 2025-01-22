from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import Post
from .models import Comment

def post_list(request):
    # Query all posts from the database
    mypost = Post.objects.all()

    # Render the template with the context
    return render(request, 'post.html', {'mypost': mypost})

def comment_list(request,id):
    # Query all comments from the database
    comment = Comment.objects.filter(TopicID=id)

    # Render the template with the context
    return render(request, 'comment.html', {'comment': comment})

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())
