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
