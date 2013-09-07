'''
Created on 2012-7-5

@author: yunify
'''
import base64
import hmac
import sys
import urllib
from qingcloud.cli.misc.utils import get_utf8_value, get_ts
from qingcloud.cli.misc.json_tool import json_dump
#
# the following is necessary because of the incompatibilities
# between Python 2.4, 2.5, and 2.6 as well as the fact that some
# people running 2.4 have installed hashlib as a separate module
# this fix was provided by boto user mccormix.
# see: http://code.google.com/p/boto/issues/detail?id=172
# for more details.
#
try:
    from hashlib import sha1 as sha
    from hashlib import sha256 as sha256

    if sys.version[:3] == "2.4":
        # we are using an hmac that expects a .new() method.
        class Faker:
            def __init__(self, which):
                self.which = which
                self.digest_size = self.which().digest_size

            def new(self, *args, **kwargs):
                return self.which(*args, **kwargs)

        sha = Faker(sha)
        sha256 = Faker(sha256)

except ImportError:
    import sha
    sha256 = None


class HmacKeys(object):
    """Key based Auth handler helper."""

    def __init__(self, host, qy_access_key_id, qy_secret_access_key, msg_time_out):
        self.host = host
        self.qy_access_key_id = qy_access_key_id
        self.qy_secret_access_key = qy_secret_access_key
        self.msg_time_out = msg_time_out
        self.update_provider(self.qy_access_key_id, self.qy_secret_access_key)

    def update_provider(self, qy_access_key_id, qy_secret_access_key):
        self.qy_access_key_id = qy_access_key_id
        self.qy_secret_access_key = qy_secret_access_key
        self._hmac = hmac.new(self.qy_secret_access_key, digestmod=sha)
        if sha256:
            self._hmac_256 = hmac.new(self.qy_secret_access_key,
                                      digestmod=sha256)
        else:
            self._hmac_256 = None

    def algorithm(self):
        if self._hmac_256:
            return 'HmacSHA256'
        else:
            return 'HmacSHA1'

    def sign_string(self, string_to_sign):
        if self._hmac_256:
            hmac = self._hmac_256.copy()
        else:
            hmac = self._hmac.copy()
        hmac.update(string_to_sign)
        return base64.b64encode(hmac.digest()).strip()

class QuerySignatureAuthHandler(HmacKeys):
    """Provides Query Signature Authentication."""

    SignatureVersion = 1
    APIVersion = 1

    def _calc_signature(self, params, verb, path):
        ''' calc signature for request '''
        string_to_sign = '%s\n%s\n' % (verb, path)
        params['signature_method'] = self.algorithm()
        keys = sorted(params.keys())
        pairs = []
        for key in keys:
            val = get_utf8_value(params[key])
            pairs.append(urllib.quote(key, safe='') + '=' +
                         urllib.quote(val, safe='-_~'))
        qs = '&'.join(pairs)
        string_to_sign += qs
        #print "string to sign:[%s]" % string_to_sign
        b64 = self.sign_string(string_to_sign)
        return (qs, b64)

    def add_auth(self, req, **kwargs):
        ''' add authorize information for request '''
        req.params['access_key_id'] = self.qy_access_key_id
        req.params['signature_version'] = self.SignatureVersion
        req.params['version'] = self.APIVersion
        time_stamp = get_ts()
        req.params['time_stamp'] = time_stamp
        #print json_dump(req.params, indent=2)
        qs, signature = self._calc_signature(req.params, req.method,
                                             req.auth_path)
        #print 'query_string: %s Signature: %s' % (qs, signature)
        if req.method == 'POST':
            req.body = json_dump(req.params)
            req.headers['Content-Length'] = str(len(req.body))
            req.headers['Content-Type'] = "application/json"
        else:
            req.body = ''
        # if this is a retried req, the qs from the previous try will
        # already be there, we need to get rid of that and rebuild it
        req.path = req.path.split('?')[0]
        req.path = (req.path + '?' + qs +
                             '&signature=' + urllib.quote_plus(signature))

