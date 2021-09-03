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

        from .containers.mapper_container import container as mapper_container
        from .containers.repo_container import container as repo_container
        from .containers.usecase_container import container as usecase_container

        usecase_container.wire(packages=[view_auth, view_member, view_admin])
        repo_container.wire(
            packages=[service_auth, service_member, service_admin])
        mapper_container.wire(
            packages=[service_auth, service_member, service_admin, mappers])
