# python's
import hashlib
# from hmac import digest

# encode a string to a hash -- encode to utf-8
encode = 'A'.encode() # no args encode to utf-8


# decode a hash to a string -- decode from utf-8
digest = hashlib.sha256(encode).hexdigest()

print(digest)
print(digest == hashlib.sha256('A'.encode()).hexdigest())