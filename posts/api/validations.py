from filters.schema import base_query_params_schema
from filters.validations import IntegerLike, DatetimeWithTZ
import six


posts_scheme = base_query_params_schema.extend(
    {
        'title' : six.text_type,
        'description' : six.text_type,
        'orden': IntegerLike(),
        'created_at': DatetimeWithTZ(),
    }

)