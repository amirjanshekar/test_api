from .base import *  # NoQA


# enable Browsable API Renderer
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] += ("rest_framework.renderers.BrowsableAPIRenderer",)  # noqa F405


INSTALLED_APPS += ["django_extensions"]  # noqa F405


CORS_ALLOW_ALL_ORIGINS = True


INTERNAL_IPS = [  # noqa F405
    "127.0.0.1",
    "localhost",
]

SWAGGER_SETTINGS = {
    "USE_SESSION_AUTH": True,
    "SECURITY_DEFINITIONS": {"Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"}},
}
