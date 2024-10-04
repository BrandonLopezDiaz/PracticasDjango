from filters.schema import base_query_params_schema
import six


temas_scheme = base_query_params_schema.extend(
    {
        'titulo' : six.text_type,
        'descripcion' : six.text_type,
        'video_url' : six.text_type,
        'imagen_url' : six.text_type,
    }
)