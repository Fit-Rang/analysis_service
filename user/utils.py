import hashlib
import base64

def generate_short_id(uuid: str):
    hash_bytes = hashlib.sha1(uuid.encode()).digest()
    encoded = base64.urlsafe_b64encode(hash_bytes).decode()
    short = encoded.rstrip('=')
    return short[:12]

