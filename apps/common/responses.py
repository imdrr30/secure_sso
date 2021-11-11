from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


def error_response(error_code, message, status_code, data=None):
    return Response(
        data={
            "status": "failed",
            "message": message,
            "error_code": error_code,
            "data": data,
        },
        status=status_code,
    )


def error_response_dispatch(error_code, message, status_code, data=None):
    response = error_response(error_code, message, status_code, data)
    response.accepted_renderer = JSONRenderer()
    response.accepted_media_type = "application/json"
    response.renderer_context = {}
    return response


def success_response(message, status_code=200, data=None):
    return Response(
        data={
            "status": "success",
            "message": message,
            "error_code": None,
            "data": data,
        },
        status=status_code,
    )
