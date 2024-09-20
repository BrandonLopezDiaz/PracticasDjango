class PostsFilter:
    ordering = ('id')
    filter_mapping = {
        'title': 'title_icontains',
        'description': 'description_icontains' ,
        'orden' : 'orden',
        'created_at': 'created_at' ,
    }