from rest_framework import serializers
from posts.models import Post
from markdown import markdown


class PostSerializer(serializers.ModelSerializer):
    """Used to serialize the output of Post for view.
    """
    content = serializers.SerializerMethodField()
    tags = serializers.SerializerMethodField()

    def get_content(self, obj):
        return markdown(obj.content)

    def get_tags(self, obj):
        return obj.tags.split(',')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'author','tags', 'content', 'created_on']


class PostListSerializer(serializers.ModelSerializer):
    """The json serialised output of the post list, and only Serialise 'id','title','url','created_on'
    """
    # url = serializers.SerializerMethodField()

    # def get_url(self, obj):
    #     return '{}'.format(obj.slug)
        # should be slug, but keep this method for future

    class Meta:
        model = Post
        fields = ['id', 'title', 'slug', 'created_on']
