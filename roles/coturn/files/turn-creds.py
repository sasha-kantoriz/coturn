import hashlib
import hmac
import base64
from time import time
import sys

user = sys.argv[1]
secret = sys.argv[2]

ttl = 24 * 3600 # Time to live
timestamp = int(time()) + ttl
username = str(timestamp) + ':' + user
dig = hmac.new(secret.encode('utf-8'), username.encode('utf-8'), hashlib.sha1).digest()
password = base64.b64encode(dig).decode()

print('username: %s' % username)
print('password: %s' % password)
