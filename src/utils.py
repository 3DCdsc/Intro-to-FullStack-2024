"""Utility functions."""

import hashlib
import os
import random

from wonderwords import RandomWord

r = RandomWord()


def random_name():
    """Generate a random name."""
    return "-".join([r.word() for _ in range(2)]) + str(random.randint(1, 100))


def hash_passwd(passwd: str):
    """Hash the password."""
    salt = os.urandom(16)
    pwhash = hashlib.pbkdf2_hmac("sha256", passwd.encode(), salt, 100000)
    method = "pbkdf2_sha256"
    return f"{method}${salt.hex()}${pwhash.hex()}"
