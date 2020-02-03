from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy
from pyramid.config import Configurator
from pyramid.session import SignedCookieSessionFactory


class MyAuthenticationPolicy(AuthTktAuthenticationPolicy):
    def authenticated_userid(self, request):
        user = request.user
        if user is not None:
            return user.id


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.set_default_csrf_options(require_csrf=True)
    authn_policy = MyAuthenticationPolicy(settings['auth.secret'], hashalg='sha512', )
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(ACLAuthorizationPolicy())
    my_session_factory = SignedCookieSessionFactory('itsaseekreet')
    config.set_session_factory(my_session_factory)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('index', '/')
    config.scan()
    return config.make_wsgi_app()
