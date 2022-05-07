import sys
import umidity

def main(args=None):
    if args is None:
        args = sys.argv[1:]
    umidity.read_data()

if __name__ == "__main__":
    sys.exit(main())