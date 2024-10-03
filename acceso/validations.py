from filters.schema import base_query_params_schema
import six


acceso_scheme = base_query_params_schema.extend(
    {
        'acceso' : six.text_type,
    }
)