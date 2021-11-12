ACTION_TYPE_TO_METHOD = {
    "list": "GET",
    "detail": "GET",
    "create": "POST",
    "update": "PUT",
    "patch": "patch",
    "delete": "DELETE",
}

METHOD_TO_ACTION_TYPE = {
    "GET": ["list", "detail"],
    "POST": ["create"],
    "PUT": ["update"],
    "DELETE": ["delete"],
    "PATCH": ["update"],
}
