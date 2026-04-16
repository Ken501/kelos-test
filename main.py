from datetime import datetime


def main():
    """Print hello world and the current date and time."""
    print("Hello, World!")
    print(f"Current date and time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


if __name__ == "__main__":
    main()
