from django.apps import AppConfig


class KafgirApiConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Kafgir_API'

    def ready(self):

        from .services import admin as service_admin
        from .services import auth as service_auth
        from .services import member as service_member

        from .views import admin as view_admin
        from .views import auth as view_auth
        from .views import member as view_member

        from . import mappers

        from .containers import container

        container.wire(packages=[service_admin, service_auth,
                                 service_member, view_auth, view_member, view_admin, mappers])
