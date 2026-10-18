import string
import secrets

def random_code_generation():
    alphabet = string.ascii_letters + string.digits
    code = ''.join(secrets.choice(alphabet) for i in range(7))

    return code