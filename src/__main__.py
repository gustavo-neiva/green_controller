import sys
from .umidity import read_data

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    read_data()

if __name__ == "__main__":
    sys.exit(main())