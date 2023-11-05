from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa 
from cryptography.hazmat.primitives import serialization

# generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
)
public_key = {
'Nelson': 'nelsonkey.pub',
'Marie': 'mariekey.pub',
'Sky': 'skykey.pub'
}
message = b'Nelson loves cat'
signature = b'Real signature'

# message validation executed by other people 
public_key.verify(
    signature,message,padding.PSS(mgf=padding.MGF1(hashes.SHA256()),
    salt_length=padding.PSS.MAX_LENGTH),
    hashes.SHA256()
)