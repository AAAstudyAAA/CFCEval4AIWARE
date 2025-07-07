"""
Authenticated HTTP proxy for Jupyter Notebooks

Some original inspiration from https://github.com/senko/tornado-proxy
"""

import inspect
import socket
import os
from urllib.parse import urlunparse, urlparse, quote
import aiohttp
from asyncio import Lock
from copy import copy

from tornado import gen, web, httpclient, httputil, process, websocket, ioloop, version_info

from jupyter_server.utils import ensure_async, url_path_join
from jupyter_server.base.handlers import JupyterHandler, utcnow
from traitlets.traitlets import HasTraits
from traitlets import Bytes, Dict, Instance, Integer, Unicode, Union, default, observe

from .utils import call_with_asked_args
from .websocket import WebSocketHandlerMixin, pingable_ws_connect
from simpervisor import SupervisedProcess


def build_proxied_client_url(self, scheme, target_host, target_port, target_path):
    if self.absolute_url:
        base_context_path = self._get_context_path(target_host, target_port)
        combined_path = url_path_join(base_context_path, target_path)
    else:
        combined_path = target_path

    # vulnerable

    # Quote spaces, åäö and such, but only enough to send a valid web
    # request onwards. To do this, we mark the RFC 3986 specs' "reserved"
    # and "un-reserved" characters as safe that won't need quoting. The
    # un-reserved need to be marked safe to ensure the quote function behave
    # the same in py36 as py37.
    #
    # ref: https://tools.ietf.org/html/rfc3986#section-2.2
    combined_path = quote(combined_path, safe=":/?#[]@!$&'()*+,;=-._~")

    proxied_url = '{protocol}://{host}:{port}{path}'.format(
        protocol=scheme,
        host=target_host,
        port=target_port,
        path=combined_path,
    )
    if self.request.query:
        proxied_url += '?' + self.request.query

    return proxied_url
