# coding=utf-8
import json
import urllib
import urllib2

from pyramid.httpexceptions import HTTPMovedPermanently
from pyramid.view import notfound_view_config, view_config



@view_config(route_name='index', renderer='templates/index.pt')
def index(request):
    return {'project': 'yottos'}


@notfound_view_config(append_slash=True)
def notfound(request):
    return HTTPMovedPermanently(location=request.route_url('index'))
