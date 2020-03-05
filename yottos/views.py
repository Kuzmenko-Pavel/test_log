# coding=utf-8
from pyramid.httpexceptions import HTTPMovedPermanently
from pyramid.view import notfound_view_config, view_config


def pretty(d, indent=0):
    if isinstance(d, dict):
        for key, value in d.items():
            print('\t' * indent + str(key))
            if isinstance(value, dict):
                pretty(value, indent + 1)
            else:
                print('\t' * (indent + 1) + str(value))
    else:
        print(d, sep='\n')


def log_request(request):
    print('='*50)
    pretty(request.path_url)
    print('---params---')
    pretty(dict(request.params))
    print('---headers---')
    pretty(dict(request.headers))
    print('---environ---')
    pretty(dict(request.environ))
    print('='*50)


@view_config(route_name='index', renderer='templates/index.pt')
def index(request):
    log_request(request)
    headers = dict(request.headers)
    environ = dict(request.environ)
    doc = {
        'A': headers.get('Accept'),
        'AL': headers.get('Accept-Language'),
        'UA': headers.get('User-Agent'),
        'AE': headers.get('Accept-Encoding'),
        'XS': environ.get('X_SSL_CERT'),
    }
    return doc


@view_config(route_name='not_found', renderer='templates/404.pt')
def not_found(request):
    # log_request(request)
    return {}


@view_config(route_name='frame', renderer='templates/frame.pt')
def frame(request):
    # log_request(request)
    return {}


@view_config(route_name='mouse', renderer='templates/frame.pt')
def mouse(request):
    # log_request(request)
    return {}


@notfound_view_config(append_slash=True)
def notfound(request):
    # log_request(request)
    return HTTPMovedPermanently(location=request.route_url('not_found'))
