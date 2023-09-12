from random import choice
import string


def generate_random_string(length: int = 6) -> str:
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits
    result_str = ''.join(choice(letters) for _ in range(length))
    return result_str
