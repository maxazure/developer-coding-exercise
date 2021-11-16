from rest_framework import serializers
from posts.models import Post
from markdown import markdown


class PostSerializer(serializers.ModelSerializer):
    """Used to serialize the output of Post for view.
    """
    html_content = serializers.SerializerMethodField()

    def get_html_content(self, obj):
        return markdown(obj.content)

    class Meta:
        model = Post
        fields = ['id', 'title', 'tags', 'html_content', 'created_on']


class PostListSerializer(serializers.ModelSerializer):
    """The json serialised output of the post list, and only Serialise 'id','title','url','created_on'
    """
    url = serializers.SerializerMethodField()

    def get_url(self, obj):
        return '{}'.format(obj.slug)
        # should be slug, but keep this method for future

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'created_on']
