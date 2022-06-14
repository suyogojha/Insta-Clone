"""Platzigram middleware catalog."""

# Django
from django.shortcuts import redirect
from django.urls import reverse


class ProfileCompletionMiddleware:
    """Profile completion middleware.

    Ensure every user that is interacting with the platform
    have their profile picture and biography.
    """

    def __init__(self, get_response):
        """Middleware initialization."""
        self.get_response = get_response

    def __call__(self, request):
        """Code to be executed for each request before the view is called."""
        if not request.user.is_anonymous:
            if not request.user.is_staff:
                profile = request.user.profile
                if not profile.picture or not profile.biography:
                    if request.path not in [reverse('users:update_profile'), reverse('users:logout')]:
                        return redirect('users:update_profile')

        response = self.get_response(request)
        return response


"""
Los Middlewares tienen el siguiente orden:

SecurityMiddleware: Se encarga de comprobar todas las medidas de seguridad, las variables de settings relacionadas con Https, Auth, entre otros.
SessionMiddleware: Se encarga de validar una sesión.
CommonMiddleware: Se encarga de verificar componentes comunes como lo es el debug.
CsrfViewMiddleware: Se encarga de toda la validación correspondiente a CSRF. Éste nos permite utilizar el tag {% csrf_token %} y es el que inserta el token de seguridad en cada formulario.
AuthenticationMiddleware: Nos permite agregar request.user desde las vistas.
MessageMiddleware: Pertenece al Framework de mensajes de Django, y permite pasar un mensaje sin necesidad de mantener un estado en la base de datos o en memoria.
XFrameOptionsMiddleware: Middleware de seguridad.

"""