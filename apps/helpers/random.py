import secrets
import string


def get_pair_code(N=8):
    return "".join(
        secrets.choice(string.ascii_uppercase + string.digits) for _ in range(N)
    )
