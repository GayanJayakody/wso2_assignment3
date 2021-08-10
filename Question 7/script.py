import hashlib
import sys, os

salt=os.urandom(32) #returns random bytes from an OS-specific randomness source. On a UNIX-like system this will query /dev/urandom, and on Windows it will use CryptGenRandom().
print((hashlib.pbkdf2_hmac('sha512', sys.argv[1].strip().encode(), salt, 200000)).hex())
