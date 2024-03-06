#!/usr/bin/env -S sh -c 'python3 "$0" "$@" || python "$0" "$@"'

"""
Module Docstring
"""

__author__ = "Your Name"
__version__ = "0.1.0"
__license__ = "MIT"

import argparse


def main():
    """Main entry point of the app"""
    args: argparse.Namespace = parse_args()
    print(getattr(args, "arg"))
    print(args.__dict__["flag"])
    print(args.name)
    # Code to execute


def parse_args():
    """Parse arguments when running from the command line"""
    parser = argparse.ArgumentParser(description="Script description")
    # Required positional argument
    parser.add_argument("arg", help="Required positional argument")
    # Optional argument flag which defaults to False
    parser.add_argument("-f", "--flag", action="store_true", default=False)
    # Optional argument which requires a parameter (eg. -d test)
    parser.add_argument("-n", "--name", action="store", dest="name")
    # Optional verbosity counter (eg. -v, -vv, -vvv, etc.)
    parser.add_argument(
        "-v", "--verbose", action="count", default=0, help="Verbosity (-v, -vv, etc)"
    )
    # Specify output of '--version'
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s (version {__version__}"
    )
    # Add more arguments if needed
    return parser.parse_args()


if __name__ == "__main__":
    main()
