import urllib.parse
import hashlib
import hmac
import base64

def get_kraken_signature(urlpath, data, secret):

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

def kraken_request(url_path,data, api_key,api_sec):
    headers = {"API-Key": api_key, "API-Sign": get_kraken_signature (url_path, data, api_sec)}
