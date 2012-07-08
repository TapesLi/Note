import string
import random

def create_url():
    letters = string.ascii_letters + string.digits
    return ''.join(random.sample(letters, 8))
