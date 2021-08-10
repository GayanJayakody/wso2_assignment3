import hashlib
import sys, os

salt=os.urandom(32) #returns random bytes from an OS-specific randomness source. On a UNIX-like system this will query /dev/urandom, and on Windows it will use CryptGenRandom().
data = sys.argv[1].strip().encode() + salt
print(hashlib.sha512( str( data ).encode("utf-8") ).hexdigest())
