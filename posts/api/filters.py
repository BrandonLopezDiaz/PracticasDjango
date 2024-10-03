import posts.api.validations as v
class PostsFilter:
    ordering = ('id')
    filter_mappings = {
        'title': 'title__icontains',
        'description': 'description__icontains' ,
        'orden' : 'orden',
        'created_at': 'created_at' ,
    }
    filter_validation_schema = v.posts_scheme