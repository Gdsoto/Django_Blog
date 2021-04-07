from blog.models import Tag, Post


def get_tags(request):
    tags_in_use = Post.objects.filter(
        public=True).values_list('tags', flat=True)
    tags = Tag.objects.filter(id__in=tags_in_use).values_list('id', 'name')
    return{
        'tags': tags,
        'ids': tags_in_use,
    }
