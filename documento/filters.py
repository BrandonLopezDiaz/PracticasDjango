class DocumentoFilter:
    ordering = ('id')
    filter_mapping = {
        'videos': 'videos__icontains',
        'pdf' : 'pdf',
        'descripcion': 'descripcion__icontains' ,
    }