import user.validations as v
class UserFilter:
    ordering = ('id')
    filter_mappings = {
        'accesos': 'accesos',
        'nombre' : 'nombre__icontains',
        'apellido' : 'apellido__icontains',
        'direccion' : 'direccion__icontains',
        'email' : 'email__icontains',
        'password' : 'password__icontains',
        'created_at' : 'created_at',
    }
    filter_validation_schema = v.user_scheme