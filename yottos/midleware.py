import logging
import time

log = logging.getLogger(__name__)


def timing_tween_factory(handler, registry):
    def timing_tween(request):
        start = time.time()
        try:
            response = handler(request)
        finally:
            end = time.time()
            log.debug('The request took %s seconds' %
                      (end - start))
        return response
    return timing_tween


def includeme(config):
    config.add_tween('yottos.midleware.timing_tween_factory')