from django.http.response import HttpResponse, JsonResponse
from posts.models import Post
from posts.serializers import PostSerializer, PostListSerializer


def post(request, slug=None):
    """Output the json of a post

    Returns:
        JsonResponse: The [data] wrapped in the returned data is for the client to identify clearly
    """    
    if request.method =='GET':
        if slug is not None:
            try:
                post = Post.objects.get(slug=slug)
            except Post.DoesNotExist:
                return HttpResponse(status=404)
            post_serializer = PostSerializer(post)
            return JsonResponse({'data':post_serializer.data}, safe=False)

        else:
            return HttpResponse(status=404)

def posts(request):
    """Output a post list json
    """
    if request.method =='GET':
        posts = Post.objects.all()
        posts_serializer = PostListSerializer(posts, many=True)
        return JsonResponse({'data':posts_serializer.data, }, safe=False)
