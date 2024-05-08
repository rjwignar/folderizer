import argparse

parser = argparse.ArgumentParser(
    prog="folderizer",
    description="File organization command-line tool.",
    epilog="Thanks for using %(prog)s!")
parser.add_argument('filepath')
parser.add_argument("-v","--version", action="version", version="%(prog)s 0.1.0")
args = parser.parse_args()

def example_function():
    return 1 + 1
