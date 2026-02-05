from functions_framework import http

@http
def starwars_api(request):
    return {"status": "ok"}
