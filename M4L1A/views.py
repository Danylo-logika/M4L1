from django.shortcuts import render, get_object_or_404
from M4L1A.models import Post
# Create your views here.
def post_list(request):
    posts = Post.objects.all()

    return render(request, template_name='index.html', context={"posts":posts})