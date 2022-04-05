__version__ = "0.1.0"

from app.mod_a import mod_a
from app.mod_b import mod_b

def main():
    print("Running app version %s." % __version__)
    print("This is a msg from the main app.py")

    mod_a.mod_a()
    mod_b.mod_b()
