infraction_insert_schema = {
    'type': 'object',
    'required': ['nom', 'adresse', 'ville', 'date_visite', 'nom_plaignant', 'description'],
    'properties': {
        'nom': {
            'type': 'string'
        },
        'adresse': {
            'type': 'string'
        },
        'ville': {
            'type': 'string'
        },
        'date_visite': {
            'type': 'string'
        },
        'nom_plaignant': {
            'type': 'string'
        },
        'description': {
            'type': 'string'
        },
    },
    'additionalProperties': False
}

infraction_delete_schema = {
    'type': 'object',
    'required': ['id'],
    'properties': {
        'id': {
            'type': 'number',
            'minimum': 0
        }
    },
    'additionalProperties': False
}
