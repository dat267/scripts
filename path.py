#!/usr/bin/env -S sh -c 'python3 "$0" "$@" || python "$0" "$@"'

import os


def main() -> None:
    script_path: str = get_current_script_path()
    print(f"Current script path: {script_path}")


def get_current_script_path() -> str:
    return os.path.abspath(__file__)


if __name__ == "__main__":
    main()
