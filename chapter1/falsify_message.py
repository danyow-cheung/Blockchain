from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives import serialization

messages = b'Nelson hates cat'
signature = b'Fake signature'

with open('nelsonkey.pub','rb') as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    ) 

public_key.verify(
    signature,
    messages,
    padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH),
                hashes.SHAKE256()
)
