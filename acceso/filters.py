import acceso.validations as v
class AccesosFilter:
    ordering = ('id')
    filter_mappings = {
        'acceso': 'acceso__icontains',
    }
    filter_validation_schema = v.acceso_scheme