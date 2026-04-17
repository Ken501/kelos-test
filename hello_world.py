"""Print hello world with the current date and time."""

from datetime import datetime


def main():
    now = datetime.now()
    print(f"Hello, World! The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
