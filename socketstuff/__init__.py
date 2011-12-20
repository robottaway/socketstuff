from pyramid.config import Configurator
from socketstuff.resources import Root

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(root_factory=Root, settings=settings)
    config.scan()
    config.add_static_view('static', 'socketstuff:static', cache_max_age=3600)
    config.add_route('boing', 'boing')
    config.add_route('socketio', 'socket.io/*remaining')
    return config.make_wsgi_app()
