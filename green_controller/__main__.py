import sys
from .app import run

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    run()

if __name__ == "__main__":
    sys.exit(main())