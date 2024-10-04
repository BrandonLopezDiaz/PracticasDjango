import temario.validations as v
class TemasFilter:
    ordering = ('id')
    filter_mappings = {
        'titulo': 'titulo__icontains',
        'descripcion': 'descripcion__icontains',
        'video_url': 'video_url__icontains',
        'imagen_url': 'imagen_url__icontains',
    }
    filter_validation_schema = v.temas_scheme