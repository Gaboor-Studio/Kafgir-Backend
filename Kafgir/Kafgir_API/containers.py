from dependency_injector import containers, providers


class Container(containers.DeclarativeContainer):
    pass

container = Container()
# container.init_resources()
