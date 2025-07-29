import sys

import requests

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    """greet function"""
    greeting = f"Hello, {who_to_greet}"
    return greeting

print(greet('Claudiu'))
print(greet('Ioana'))

r = requests.get("https://coreyms.com")
print(r.status_code)
