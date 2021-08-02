import hashlib
import sys

salt="Km5d5ivMy8iexuHcZrsD"

print((hashlib.pbkdf2_hmac('sha512', sys.argv[0].strip().encode(), salt.encode(), 200000)).hex())