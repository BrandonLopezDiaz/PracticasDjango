from filters.schema import base_query_params_schema
import six
from filters.validations import (
    IntegerLike,
    DatetimeWithTZ
)

user_scheme = base_query_params_schema.extend(
    {
        "id": IntegerLike(),
        'acceso' : IntegerLike(),
        'nombre' : six.text_type,
        'apellido' : six.text_type,
        'direccion' : six.text_type,
        'email' : six.text_type,
        'password' : six.text_type,
        'created_at' : DatetimeWithTZ(),
    }
)