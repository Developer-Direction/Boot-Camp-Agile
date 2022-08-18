import urllib.parse
import hashlib
import hmac
import base64
import time


kraken_data = {
  "nonce": str(int(1000*time.time()))
}

def get_kraken_signature(urlpath, data, secret):

    postdata = urllib.parse.urlencode(data)
    encoded = (str(data['nonce']) + postdata).encode()
    message = urlpath.encode() + hashlib.sha256(encoded).digest()

    mac = hmac.new(base64.b64decode(secret), message, hashlib.sha512)
    sigdigest = base64.b64encode(mac.digest())
    return sigdigest.decode()

def kraken_request(url_path,data, api_key,api_sec):
    headers = {"API-Key": api_key, "API-Sign": get_kraken_signature (url_path, data, api_sec)}


def get_kraken_data():
    return kraken_data