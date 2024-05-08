import argparse

parser = argparse.ArgumentParser(
    prog="folderizer",
    description="File organization command-line tool.",
    epilog="Thanks for using %(prog)s!")
parser.add_argument('filepath')
args = parser.parse_args()

def example_function():
    return 1 + 1
